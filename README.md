# Kovarik Bioinformatics Testing for NuProbe Scientist I

![image](https://github.com/denkovarik/Kovarik-BI-Testing-for-NuProbe-Scientist-I/blob/main/images/BI.png)

## Introduction
This project is the Bioinformatics Testing for NuProbe Scientist I for Dennis Kovarik. This project was completed on 7/12/2021.

PCR is a procedure where scientists amplify target sequences to perform further study. One reason they my want amplification is if they wanted to align these sequences to determine their homology and/or similarity to each other. Software such as Bowtie2 will attempt to align amplicons, but at times it will fail to align some sequences. This non-specific amplification is bad because it can suppress the on-target amplification, which would increase non-uniformity and increase costs. Because of this, it is important to try to remove the primers that caused to amplification of these unaliged amplicaons. Doing this would help produce better results from PCR amplification by promoting uniformity and decreasing costs.

This project attempts to do just that! Given the results from the Bowtie2 software and a list of primers, this software attempts to identify the primer pairs that led to the non-specific amplification. Some of the assumptions made in the process are as follows:

1. There is no adapter, meaning that the forward and reverse primers start and the very ends of the sequence. 
2. Further, a complete match between the primers and sequence where requiired before being considered a match.

Now in reality, some mismatches between the primer and target sequence may be tolerated, but by enforcing a complete match between the primer pairs and the sequence, we do to things that are beneficial.

1. We limit the number of False Positive matches between the primers and thee sequence. The less mismatches we have, the less likely a primer will be falsely identified as binding to a sequence.
2. By enforcing a complete match, we can do a binary search for a match, which would save time. 

By doing this, this software can help researchers identify primers that might be negatively affecting their PCR results.

## Setup
This project was developed for the Ubuntu 20.04 OS.

### Dependences
* Git
* Python 3.8
* pysam
* plotly
* NumPy
* openpyxl
* progress
* tqdm
* Pandas
* openyxl

### Cloning This Repo with HTTPS
To download this repository on your device, you must clone this repo using either HTTPS or SSH. The easiest way to clone this repository on your local device is through HTTPS. If you SDK allows you to clone a repo through HTTPS, then do so. Otherwise, you can do it directly on the command prompt. To do so, open up the command prompt and move to the desired directory. Then simply run the following command and enter you credentials.
```
git clone https://github.com/denkovarik/Kovarik-BI-Testing-for-NuProbe-Scientist-I.git
```
After the repo has been cloned on your device, move into the Kovarik-Technical-Interview directory from the command line.
```
cd Kovarik-BI-Testing-for-NuProbe-Scientist-I
```

### Cloning This Repo with SSH
You can also clone this repo using SSH. Follow the instructions below to clone the repo using SSH. Please note that if you have already cloned the repo using HTTPS, then you can skip to the 'Install Dependencies' step.

#### Generate an SSH Key Pair
In order to clone this repository, you need to add your public SSH key to this repo. If you don't have one, then you would need to generate one. [How to Generate SSH key in Windows 10? Easy Methods!!](https://techpaal.com/how-to-generate-ssh-key-in-windows-10-easy-methods/) should help you generate an SSH key pair.

#### Add Your Public SSH Key to GitHub
Once you have an SSH Key Pair generated, you need to add your public SSH key to GitHub. Follow [How to view your SSH keys in Linux, macOS, and Windows](https://www.techrepublic.com/article/how-to-view-your-ssh-keys-in-linux-macos-and-windows/) to access you public key. Then follow [Adding a new SSH key to your GitHub account](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) to add your public SSH key to GitHub.

#### Clone the Repository
If your SDK allows for it, then clone this repository through you SDK. Otherwise, open up the command prompt, move the the directory of your choice, then run the following command.
```
git git@github.com:denkovarik/Kovarik-BI-Testing-for-NuProbe-Scientist-I.git
```
After the repo has been cloned on your device, move into the Bioinformatics-Tools directory from the command line.
```
cd Kovarik-BI-Testing-for-NuProbe-Scientist-I
```

### Install Dependencies
```
./setup/setup.sh
```

## Usage
This program can be run without any command line arguemtns. As a result the program will run on the example files.
```
python find_unaligned_amplicon_primers.py 
```

### Command Line Arguments Supported
```
find_unaligned_amplicon_primers.py --bowtie2_rslt_path <filepath to Bowtie2 results>                                                                          --primers_path <filepath to the .xlsx file holding the primers>
                                   --output_NS_pairs <path to NS Pairs excel file>
                                   --output_NS_list <path to NS List excel file>
                                   --heat_map <path to the heat map>
```

### Output from Program
As a result of running this program, 2 output excel files and a heat map will be produced. By default, they output files can be found in the my_output/, but this can also be changed. The file output_NS_list.xlsx is simply a list of the unique sequences along with the forward, reverse primers, and some stats. The file output_NS_pairs.xlsx lists the unique primer pairs that make them up along with more states. Finally, a heat map is generated to give a visual representation of the results and provide insight into which primer pairs actually match with a sequence. 

![image](https://raw.githubusercontent.com/denkovarik/Kovarik-BI-Testing-for-NuProbe-Scientist-I/main/images/heat_map.png?token=AJUAOAVGHCPFRHQ6ISBIIY3A5PZOC)

## Testing
### Run All Tests
```
./teseting/run_tests.sh 
```

### Run testing for Amplicon class
```
testing/Amplicon_tests.py 
```

### Run testing for Forward_Primer class
```
testing/Forward_Primer_tests.py
```

### Run testing for Reverse_Primer class
```
testing/Reverse_Primer_tests.py
```

### Run testing for Sequence_tests.py class
```
testing/Sequence_tests.py
```

## Author
* Dennis Kovarik
