# CC WANT PBJ

## Downloading the config file.
   
  - download the git repository.
  
    ```
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
   cmsRun python/poet_cfg.py
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
   cmsRun python/poet_cfg.py
   ```
5. A ROOT file named "myoutput.root" will be created.

## Create Invariant Mass plot.

1. Copy `mass.py` to the directory that `myoutput.root` lives in.

2. Run the script `mass.py` as shown below.

	```bash
	python -i mass.py
	```

3. A canvas will open with the plot as can be seen [here](https://github.com/JOTELLECHEA/myCMS/blob/main/example1.pdf).

## Pictures

- [Ivariant Mass](https://github.com/JOTELLECHEA/myCMS/blob/main/example1.pdf)



