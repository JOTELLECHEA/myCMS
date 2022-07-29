# CC WANT PBJ
## Have to obtain PhysObjectExtractorTool.
1. Obtain the code from git, then switch to the 2015MiniAOD Branch.
	```bash
	git clone git://github.com/cms-legacydata-analyses/PhysObjectExtractorTool.git
	cd PhysObjectExtractorTool
	git checkout 2015MiniAOD
	```
2. Make sure you are in the /PhysObjectExtractorTool when you use scram.
	```bash 
	scram b
	```
3. Make sure you have the validation file 'Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_v2.txt'.
	It should be in this directory```/PhysObjectExtractorTool/PhysObjectExtractor/data/```

## Downloading the config file.
   
  - download the git repository.
  
   ```bash
   git clone https://github.com/JOTELLECHEA/myCMS.git
   cd myCMS
   ls
   ```
    Here you can copy the `python/poet_cfg.py` to your enviroment.

## Create ROOT file from CMS OpenData for a single run.

1. Find data events of intreset on [CMS OpenData](https://opendata.cern.ch/).

2. Edit poet_cfg.py via vim/nano. Change the file you want via the xrootd protocol (root://)

   Example:
   ```python
   if isData:
		process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring("root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleEG/MINIAOD/08Jun2016-v1/10000/00387F48-342F-E611-AB5D-0CC47A4D76AC.root")
   ```
3. Type the following to create ROOT file

   ```bash
   cmsRun python/poet_cfg.py True
   ```
4. A ROOT file named "myoutput.root" will be created.

## Create ROOT file from CMS OpenData for multiple runs.

1. Find data events of intreset on [CMS OpenData](https://opendata.cern.ch/).

2. Download the file indexes to [`data/`](https://github.com/JOTELLECHEA/myCMS/tree/main/data)

3. Edit poet_cfg.py via vim/nano. Add the file index as shown below:
	- For 1 index file. 

  	   Example:
	   ```python
	   if isData:
	    files = FileUtils.loadListFromFile("data/CMS_Run2015D_DoubleEG_MINIAOD_08Jun2016-v1_10000_file_index.txt")
	    process.source = cms.Source("PoolSource", fileNames=cms.untracked.vstring(*files))
	   ```
	   * Look at rootFiles.py script to use a select count of files in index by creating a new text file. 
	- For more than 1 index file, you can extend more files.
		Example:
		```python
		if isData:
	    files = FileUtils.loadListFromFile("data/CMS_Run2015D_DoubleEG_MINIAOD_08Jun2016-v1_10000_file_index.txt")
	    files.extend(FileUtils.loadListFromFile("data/CMS_Run2015D_DoubleEG_MINIAOD_08Jun2016-v1_40000_file_index.txt"))
	    files.extend(FileUtils.loadListFromFile("data/CMS_Run2015D_DoubleEG_MINIAOD_08Jun2016-v1_70000_file_index.txt"))
	    files.extend(FileUtils.loadListFromFile("data/CMS_Run2015D_DoubleEG_MINIAOD_08Jun2016-v1_80000_file_index.txt"))
	    files.extend(FileUtils.loadListFromFile("data/CMS_Run2015D_DoubleEG_MINIAOD_08Jun2016-v1_80001_file_index.txt"))
	    process.source = cms.Source("PoolSource", fileNames=cms.untracked.vstring(*files))
	    ```

4. Then type the following to create ROOT file

   ```bash
   cmsRun python/poet_cfg.py True
   ```
5. A ROOT file named "myoutput.root" will be created.

## Create Invariant Mass plot.

1. Copy `mass.py` to the directory that `myoutput.root` lives in.

2. Run the script `mass.py` as shown below:
	- To open `myoutput.root` by default use the command below.

	```bash
	python -i mass.py
	```
	- To open a different ROOT file; pass the file to the script as shown below:
	```bash
	python -i mass.py test.root
	```

3. A canvas will open with the plot as can be seen [here](https://github.com/JOTELLECHEA/myCMS/blob/main/example1.pdf).


## rootFiles.py

A script that makes creates a new text file from CMS OpenData index files. To create a new file called `myRootFiles.txt`.

- To run script change the index file on line 11 to the index file of your choice.
- Then run the script for the files in line 13 to 33. 
	```python 
	python rootFiles.py 13 33 
	``` 
	Now a new file named `myRootFiles.txt` will be created if it already exist then it will be overwritten.

## Pictures

- [Ivariant Mass](https://github.com/JOTELLECHEA/myCMS/blob/main/zboson/plots/example1.pdf)
- [Index files](https://github.com/JOTELLECHEA/myCMS/blob/main/zboson/plots/example2.png)



