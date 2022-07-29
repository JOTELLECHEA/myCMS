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

c1 = ROOT.TCanvas('c1','Canvas 1',700,900)
c1.Divide(1,3,0.01,0.01,0)

#create a empty histogram
h1 = ROOT.TH1D('2e','2e;M_{ee} [GeV/c^{2}];Events/Bin',120,0,120)
h2 = ROOT.TH1D('2e [e^{+}e^{-}]','2e [e^{+}e^{-}];M_{ee} [GeV/c^{2}];Events/Bin',120,0,120)
h3 = ROOT.TH1D('2e [e^{+}e^{-}] and pT > 25 GeV','2e [e^{+}e^{-}] and pT > 25 GeV;M_{Z} [GeV/c^{2}];Events/Bin',120,0,120)

#loop through the entries of the leaf and fill the histogram with data∏
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
    if event.numberelectron != 2:continue
    lep4vec[0].SetPtEtaPhiM(event.electron_pt[0],event.electron_eta[0],event.electron_phi[0],0)
    lep4vec[1].SetPtEtaPhiM(event.electron_pt[1],event.electron_eta[1],event.electron_phi[1],0)
    h1.Fill((lep4vec[0]+lep4vec[1]).M())
    if event.electron_ch[0] * event.electron_ch[1] == 1:continue
    h2.Fill((lep4vec[0]+lep4vec[1]).M())
    if (event.electron_pt[0] and event.electron_pt[1]) < 25:continue
    h3.Fill((lep4vec[0]+lep4vec[1]).M())

histCount = int(h1.GetEntries())
print('There are',histCount,'events with two electrons.\n')
print('Creating Invariant Mass Plot.')

c1.cd(1)
h1.Draw()
c1.cd(2)
h2.Draw()
c1.cd(3)
h3.Draw()
c1.SaveAs("plots/InvariantMassPlot.pdf")


