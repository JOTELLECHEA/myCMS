# CC WANT PBJ
## Create ROOT files from CMS OpenData
1. Find data events of intreset on [CMS OpenData](https://opendata.cern.ch/).
![]()
2. Edit poet_cfg.py with ROOT file.
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
3. Type the following to create ROOT file

   ```
   cmsRun python/poet_cfg.py
   ```

4. A ROOT file named "myoutput.root" will be created.