#Program that outputs a histogram of the Zee_0 invariant mass
from ROOT import TCanvas,TH1F
import ROOT
import sys
import time

if len(sys.argv) > 1:
    fileName = sys.argv[1]
    print('Opening:',fileName,'\n')

else:
    fileName = 'myoutput.root'
    print('No Arguments Passed.\nOpenign default file: myoutput.root')




#opens the root file
f = ROOT.TFile(fileName)

#loads TTree into the memory
MyTree = f.Get('myelectrons/Events')
print('Found myelectron TTree.\n')

#create a empty histogram
h = ROOT.TH1D('mass','mass;Invariant Mass[GeV];Events/Bin',120,0,120)

#loop through the entries of the leaf and fill the histogram with data
#then draw histogram

entries = MyTree.GetEntries()
print('Found',entries,'envents.\n')

#declare variables

for event in MyTree:
   lep4vec = {}
   lep4vec[0] = ROOT.TLorentzVector()
   lep4vec[1] = ROOT.TLorentzVector()
   eesum = 0
   epxsum= 0
   epysum=0
   epzsum =0
   mass =0
   if event.numberelectron == 2:
       lep4vec[0].SetPtEtaPhiM(event.electron_pt[0],event.electron_eta[0],event.electron_phi[0],0)
       lep4vec[1].SetPtEtaPhiM(event.electron_pt[1],event.electron_eta[1],event.electron_phi[1],0)
       h.Fill((lep4vec[0]+lep4vec[1]).M())

histCount = int(h.GetEntries())
print('There are',histCount,'events with two electrons.\n')
print('Creating Invariant Mass Plot.')
time.sleep(3)
h.Draw()

