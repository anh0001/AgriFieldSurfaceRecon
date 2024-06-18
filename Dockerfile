# Use the official CUDA image from NVIDIA with Anaconda
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

# Set up environment variables
ENV PATH /opt/conda/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA false

# Install dependencies
RUN apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub && \
    apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    wget \
    git \
    ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -a -y && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

# Set up the working directory
WORKDIR /workspace

# Copy the contents of the repository to the container
COPY . /workspace

# Create and activate conda environment using environment.yaml
RUN /bin/bash -c "source ~/.bashrc && conda env create -f environment.yaml && conda clean -a -y"

# Set entrypoint to run bash
ENTRYPOINT [ "/bin/bash" ]
