installation
============


Download:
_________
dmr_analysis is written in python. It can be installed and accessed from command line and is available for both linux and mac operating systems. 

Please send email to Dr. Junbai Wang (junbai.wang@medisin.uio.no) for requesting a free download of DMR-analysis pacakge.

Please include your name, Institution/company name, Email of your institute or company (do not use gmail or yahoo email etc), and a brief description of the purpose for using bpb3 package.

Please use the subject title "bpb3/dds request "  for your email.

Install:
________

It is highly recommended to create a separate virtual environment for the package to avoid any library conflicts problem. You can create a virtual environment using the following commands. We recommend installing and using miniconda/anaconda (`https://docs.conda.io/en/latest/miniconda.html`). Tutorial of creating and updating virtual commands can be found at (`https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html`).

If miniconda is already installed, then you can proceed with the following step-by-step installation. We have already provided a quick installation setup file named ``quick_install.sh`` for your ease. A simple bash command will do everything automatically and prepare the package, ready to run.

.. code-block:: bash

    ./quick_install

However, step-by-step details are given as under and can be followed if ``quick_install.sh`` is unsuccessful:

.. code-block:: bash

    conda create --name dmr_env python==3.9.16
    conda activate dmr_env

Install pip if not already installed:

.. code-block:: bash

    conda install pip

Please allow any other installations when prompted.

Requirements:
_____________

Prior to installing the package, dependencies must be fulfilled. It is advised to install dependencies using miniconda. The list of dependencies is as follows:

- matplotlib==3.5.3
- numpy==1.21.5
- pandas==1.4.4
- scikit_learn==1.2.2
- scipy==1.9.1
- setuptools==65.6.3
- statsmodels==0.13.5
- bedtools==2.27.0

These dependencies can be installed one by one using the conda manager. For example:

.. code-block:: bash

    conda install numpy==1.21.5

A ``requirements.txt`` file is given with the package. All requirements can be automatically installed using one command:

.. code-block:: bash

    conda install --file requirements.txt

Or they can be installed using pip.

.. code-block:: bash

    pip install numpy==1.21.5

A ``requirements.txt`` file is given with the package. All requirements can be automatically installed using one command:

.. code-block:: bash

    pip install -r requirements.txt

You can install the package using the following command. Go to the dmr_analysis directory (folder containing setup.py and pyproject.toml) and type the following command:

.. code-block:: bash

    pip install .

For more details, follow the readme file in the package.
