# CC WANT PBJ
## Create ROOT files from CMS OpenData for a single run.
1. Find data events of intreset on [CMS OpenData](https://opendata.cern.ch/).

2. Edit poet_cfg.py via vim/nano. Change the file you want via the xrootd protocol (root://)

   Example:
   ```
   process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring("root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleEG/MINIAOD/08Jun2016-v1/10000/00387F48-342F-E611-AB5D-0CC47A4D76AC.root")
   ```
3. Type the following to create ROOT file

   ```
   cmsRun python/poet_cfg.py
   ```
## Create ROOT files from CMS OpenData for multiple runs.
1. Find data events of intreset on [CMS OpenData](https://opendata.cern.ch/).

2. Edit poet_cfg.py via vim/nano. Change the file you want via the xrootd protocol (root://)

   Example:
   ```
   process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring("root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleEG/MINIAOD/08Jun2016-v1/10000/00387F48-342F-E611-AB5D-0CC47A4D76AC.root")
   ```
3. Type the following to create ROOT file

   ```
   cmsRun python/poet_cfg.py
   ```
4. A ROOT file named "myoutput.root" will be created.
   ```
   if isData:
    files = FileUtils.loadListFromFile("data/CMS_Run2015D_DoubleEG_MINIAOD_08Jun2016-v1_10000_file_index.txt")
    files.extend(FileUtils.loadListFromFile("data/CMS_Run2015D_DoubleEG_MINIAOD_08Jun2016-v1_40000_file_index.txt"))
    files.extend(FileUtils.loadListFromFile("data/CMS_Run2015D_DoubleEG_MINIAOD_08Jun2016-v1_70000_file_index.txt"))
    files.extend(FileUtils.loadListFromFile("data/CMS_Run2015D_DoubleEG_MINIAOD_08Jun2016-v1_80000_file_index.txt"))
    files.extend(FileUtils.loadListFromFile("data/CMS_Run2015D_DoubleEG_MINIAOD_08Jun2016-v1_80001_file_index.txt"))
    #files.extend(FileUtils.loadListFromFile("data/"))
    process.source = cms.Source("PoolSource", fileNames=cms.untracked.vstring(*files))
   ```
## Pictures
- [Ivariant Mass](https://github.com/JOTELLECHEA/myCMS/blob/main/example1.pdf)