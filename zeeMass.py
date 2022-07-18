#Program that outputs a histogram of the Zee_0 invariant mass
from ROOT import TCanvas,TH1F
import ROOT
import math

#opens the root file
f = ROOT.TFile("/home/cmsusr/CMSSW_7_6_7/src/PhysObjectExtractorTool/myoutput.root")

#loads TTree into the memory
MyTree = f.Get("myelectrons/Events")

#create a empty histogram
h1 = ROOT.TH1D("number of electrons","number of electrons;#electron in events;Events/Bin",5,0,5)
h2 = ROOT.TH1D("mass","mass;Invariant Mass[GeV];Events/Bin",120,0,120)

#loop through the entries of the leaf and fill the histogram with data
#then draw histogram

entries = MyTree.GetEntries()

#declare variables

for event in MyTree:
  # h1.Fill(event.numberelectron)
   lep4vec = {}
   lep4vec[0] = ROOT.TLorentzVector()
   lep4vec[1] = ROOT.TLorentzVector()
   eesum = 0
   epxsum= 0
   epysum=0
   epzsum =0
   mass =0
   if event.numberelectron == 2:
       # eesum = event.electron_e[0] + event.electron_e[1]
#	epxsum = event.electron_px[0] + event.electron_px[1]
#        epysum = event.electron_py[0] +	event.electron_py[1]
#        epzsum = event.electron_pz[0] +	event.electron_pz[1]
#	mass = math.sqrt(pow(eesum,2) - pow(epxsum,2) -pow(epysum,2) - pow(epzsum,2) )
#	h2.Fill(mass)
       lep4vec[0].SetPtEtaPhiM(event.electron_pt[0],event.electron_eta[0],event.electron_phi[0],0)
       lep4vec[1].SetPtEtaPhiM(event.electron_pt[1],event.electron_eta[1],event.electron_phi[1],0)
       h2.Fill((lep4vec[0]+lep4vec[1]).M())


h2.Draw()
#h1.Draw()
