import FWCore.ParameterSet.Config as cms

Scale = '1.0'       # The "Scale" argument should be set to 1.0 if you want to reweight to exactly the 
                   #input data distribution. If you are evaluating systematic errors, you can use this factor
                   #to scale the distribution before the weights are calculated (i.e., correctly) by putting in a non-unity argument. 


NtupleMaker = cms.EDProducer('TauNtuple',
                             primVtx = cms.InputTag("offlinePrimaryVertices"),
                             hpsTauProducer=cms.InputTag("hpsPFTauProducer","", "TauNtupleProcess"),
                             beamSpot = cms.InputTag("offlineBeamSpot"),
                             hpsPFTauDiscriminationByTightIsolation =cms.InputTag("hpsPFTauDiscriminationByTightIsolation","", "TauNtupleProcess"), 
                             hpsPFTauDiscriminationByMediumIsolation=cms.InputTag("hpsPFTauDiscriminationByMediumIsolation","", "TauNtupleProcess"),
                             hpsPFTauDiscriminationByLooseIsolation =cms.InputTag("hpsPFTauDiscriminationByLooseIsolation","", "TauNtupleProcess"),
                             hpsPFTauDiscriminationByVLooseCombinedIsolationDBSumPtCorr=cms.InputTag("hpsPFTauDiscriminationByVLooseCombinedIsolationDBSumPtCorr","", "TauNtupleProcess"), 
                             hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr =cms.InputTag("hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr","", "TauNtupleProcess"), 
                             hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr=cms.InputTag("hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr","", "TauNtupleProcess"),
                             hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr =cms.InputTag("hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr","", "TauNtupleProcess"),
                             hpsPFTauDiscriminationAgainstElectronLoose=cms.InputTag("hpsPFTauDiscriminationByLooseElectronRejection","", "TauNtupleProcess"),
                             hpsPFTauDiscriminationAgainstElectronMedium=cms.InputTag("hpsPFTauDiscriminationByMediumElectronRejection","", "TauNtupleProcess"),
                             hpsPFTauDiscriminationAgainstElectronTight=cms.InputTag("hpsPFTauDiscriminationByTightElectronRejection","", "TauNtupleProcess"),
                             hpsPFTauDiscriminationAgainstMuonLoose=cms.InputTag("hpsPFTauDiscriminationByLooseMuonRejection","", "TauNtupleProcess"),
                             hpsPFTauDiscriminationAgainstMuonMedium=cms.InputTag("hpsPFTauDiscriminationByMediumMuonRejection","", "TauNtupleProcess"),
                             hpsPFTauDiscriminationAgainstMuonTight=cms.InputTag("hpsPFTauDiscriminationByTightMuonRejection","", "TauNtupleProcess"),
                             hpsPFTauDiscriminationByDecayModeFinding =cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding","", "TauNtupleProcess"),
                             pfMet = cms.InputTag('pfMet'),
                             muons   = cms.InputTag('muons'),
#                             kinematicTaus  = cms.InputTag("KinematicTauBasicProducer"),
                             kinematicTausAdvanced = cms.InputTag("KinematicTauProducer","KinematicFitTau"),
#                             kinematicTausAdvanced = cms.InputTag("KinematicTauProducer","SelectedKinematicDecays"),
#                             tauPrimaryVtx  = cms.InputTag("ThreeProngInputSelectorStep2","primVtx"),
                             tauPrimaryVtx  = cms.InputTag("offlinePrimaryVertices"),
                             pfMetCorrT0rt = cms.InputTag("pfMetT0rt"),
                             pfMetCorrT0rtT1 = cms.InputTag("pfMetT0rtT1"),
                             pfMetCorrT0pc = cms.InputTag("pfMetT0pc"),
                             pfMetCorrT0pcT1 = cms.InputTag("pfMetT0pcT1"),
                             pfMetCorrT0rtTxy = cms.InputTag("pfMetT0rtTxy"),
                             pfMetCorrT0rtT1Txy = cms.InputTag("pfMetT0rtT1Txy"),
                             pfMetCorrT0pcTxy = cms.InputTag("pfMetT0pcTxy"),
                             pfMetCorrT0pcT1Txy = cms.InputTag("pfMetT0pcT1Txy"),
                             pfMetCorrT1  = cms.InputTag("pfMetT1"),
                             pfMetCorrT1Txy  = cms.InputTag("pfMetT1Txy"),
                             caloMetCorrT1 = cms.InputTag("caloMetT1"),
                             caloMetCorrT1T2 = cms.InputTag("caloMetT1T2"),
                             pfMetCorrMVA  = cms.InputTag("pfMEtMVA"),
                             muonsForPfMetCorrMVA = cms.InputTag("isomuons"),
                             tausForPfMetCorrMVA = cms.InputTag("isotaus"),
                             elecsForPfMetCorrMVA = cms.InputTag("isoelectrons"),
                             pfMetCorrMVAMuTau  = cms.InputTag("pfMetMVAMuTau"),
                             muonsForPfMetCorrMVAMuTau = cms.InputTag("mvaMETMuons"),
                             tausForPfMetCorrMVAMuTau = cms.InputTag("mvaMETTausMT"),
                             pfMetUncorr  = cms.InputTag("pfMet"),
                             patMetCorrT0rt = cms.InputTag("patPfMetT0rt"),
                             patMetCorrT0rtT1 = cms.InputTag("patPfMetT0rtT1"),
                             patMetCorrT0pc = cms.InputTag("patPfMetT0pc"),
                             patMetCorrT0pcT1 = cms.InputTag("patPfMetT0pcT1"),
                             patMetCorrT0rtTxy = cms.InputTag("patPfMetT0rtTxy"),
                             patMetCorrT0rtT1Txy = cms.InputTag("patPfMetT0rtT1Txy"),
                             patMetCorrT0pcTxy = cms.InputTag("patPfMetT0pcTxy"),
                             patMetCorrT0pcT1Txy = cms.InputTag("patPfMetT0pcT1Txy"),
                             patMetCorrT1  = cms.InputTag("patPfMetT1"),
                             patMetCorrT1Txy  = cms.InputTag("patPfMetT1Txy"),
                             patCaloMetCorrT1 = cms.InputTag("patCaloMetT1"),
                             patCaloMetCorrT1T2 = cms.InputTag("patCaloMetT1T2"),
                             patMetCorrMVA = cms.InputTag("patMVAMet"),
                             patMetCorrMVAMuTau = cms.InputTag("patMVAMetMuTau"),
                             patMetUncorr = cms.InputTag("patMet"),
                             patMETType1Corr = cms.InputTag("patType1CorrectedPFMet"),
                             patMETType1p2Corr = cms.InputTag("patType1p2CorrectedPFMet"),
                             patMETType1CorrEleEnUp = cms.InputTag("patType1CorrectedPFMetElectronEnUp"),
                             patMETType1CorrEleEndown = cms.InputTag("patType1CorrectedPFMetElectronEnDown"),
                             patMETType1CorrMuEnUp = cms.InputTag("patType1CorrectedPFMetMuonEnUp"),
                             patMETType1CorrMuEnDown = cms.InputTag("patType1CorrectedPFMetMuonEnDown"),
                             patMETType1CorrTauEnUp = cms.InputTag("patType1CorrectedPFMetTauEnUp"),
                             patMETType1CorrTauEnDown = cms.InputTag("patType1CorrectedPFMetTauEnDown"),
                             patMETType1CorrJetResUp = cms.InputTag("patType1CorrectedPFMetJetResUp"),
                             patMETType1CorrJetResDown = cms.InputTag("patType1CorrectedPFMetJetResDown"),
                             patMETType1CorrJetEnUp = cms.InputTag("patType1CorrectedPFMetJetEnUp"),
                             patMETType1CorrJetEnDown = cms.InputTag("patType1CorrectedPFMetJetEnDown"),
                             patMETType1CorrUnclusteredUp = cms.InputTag("patType1CorrectedPFMetUnclusteredEnUp"),
                             patMETType1CorrUnclusteredDown = cms.InputTag("patType1CorrectedPFMetUnclusteredEnDown"),
                             patMETType1p2CorrEleEnUp = cms.InputTag("patType1p2CorrectedPFMetElectronEnUp"),
                             patMETType1p2CorrEleEndown = cms.InputTag("patType1p2CorrectedPFMetElectronEnDown"),
                             patMETType1p2CorrMuEnUp = cms.InputTag("patType1p2CorrectedPFMetMuonEnUp"),
                             patMETType1p2CorrMuEnDown = cms.InputTag("patType1p2CorrectedPFMetMuonEnDown"),
                             patMETType1p2CorrTauEnUp = cms.InputTag("patType1p2CorrectedPFMetTauEnUp"),
                             patMETType1p2CorrTauEnDown = cms.InputTag("patType1p2CorrectedPFMetTauEnDown"),
                             patMETType1p2CorrJetResUp = cms.InputTag("patType1p2CorrectedPFMetJetResUp"),
                             patMETType1p2CorrJetResDown = cms.InputTag("patType1p2CorrectedPFMetJetResDown"),
                             patMETType1p2CorrJetEnUp = cms.InputTag("patType1p2CorrectedPFMetJetEnUp"),
                             patMETType1p2CorrJetEnDown = cms.InputTag("patType1p2CorrectedPFMetJetEnDown"),
                             patMETType1p2CorrUnclusteredUp = cms.InputTag("patType1p2CorrectedPFMetUnclusteredEnUp"),
                             patMETType1p2CorrUnclusteredDown = cms.InputTag("patType1p2CorrectedPFMetUnclusteredEnDown"),
                             pfjets         = cms.InputTag("ak5PFJetsCorr"),
                             genjets        = cms.InputTag("ak5GenJets"),
                             genjetsNoNu    = cms.InputTag("ak5GenJetsNoNu"),
                             pfelectrons =  cms.InputTag("gsfElectrons",""),
                             generalTracks  = cms.InputTag("generalTracks"),
                             gensrc         = cms.InputTag('genParticles'),
                             GenEventInfo   = cms.InputTag('generator'),
                             jetFlavour     = cms.InputTag('PFAK5byValAlgo'),
                             discriminators = cms.vstring("PFRecoTauDiscriminationByKinematicFit","PFRecoTauDiscriminationByKinematicFitQuality"),
                             do_MCComplete  = cms.untracked.bool(True),
                             MCCompletePtCut = cms.double(2.5),
                             do_MCSummary   = cms.untracked.bool(True),
                             ScaleFactor    = cms.untracked.string(Scale),
                             PUInputHistoMC    = cms.untracked.string("MC_Summer12"),
                             PUInputHistoData  = cms.untracked.string("h_190456_20868"),
                             PUInputHistoData_p5 = cms.untracked.string("h_190456_20868_p5"),
                             PUInputHistoData_m5 = cms.untracked.string("h_190456_20868_m5"),
                             PUInputHistoMCFineBins = cms.untracked.string(""),
                             PUInputHistoDataFineBins = cms.untracked.string(""),
                             PUOutputFile  = cms.untracked.string("Weight3D.root"),
                             PUInputFile = cms.untracked.string("$CMSSW_BASE/src/data/Lumi_190456_208686MC_PU_S10_andData.root"),
                             TriggerProcessName = cms.untracked.string("HLT"),
                             TriggerInfoName = cms.InputTag("TrigFilterInfo","TriggerFilterInfoList"),
                             TriggerEvent = cms.InputTag("hltTriggerSummaryAOD","","HLT"), 
                             TriggerResults = cms.InputTag("TriggerResults","","HLT"),
                             L1GtTriggerMenuLite = cms.InputTag("l1GtTriggerMenuLite"),
                             l1TriggerNames = cms.vstring("L1_DoubleTau44er","L1_DoubleJetC64"),
                             RhoIsolAllInputTag   =  cms.InputTag('kt6PFJets', 'rho', 'RECO'),
                             TriggerJetMatchingdr = cms.untracked.double(0.3),
                             TriggerMuonMatchingdr = cms.untracked.double(0.3),
                             TriggerElectronMatchingdr = cms.untracked.double(0.3),
                             TriggerTauMatchingdr = cms.untracked.double(0.3),
                             BTagAlgorithm = cms.untracked.string("MyCombinedSecondaryVertexBJetTags"),
                             PUJetIdDisc = cms.InputTag("pileupJetIdProducer","fullDiscriminant"),
                             PUJetIdFlag = cms.InputTag("pileupJetIdProducer","fullId"),
                             MuonPtCut = cms.double(3.0),
                             MuonEtaCut = cms.double(2.5),
                             TauPtCut = cms.double(18.0),
                             TauEtaCut = cms.double(2.4),
                             ElectronPtCut = cms.double(8.0),
                             ElectronEtaCut = cms.double(2.5),
                             JetPtCut = cms.double(18.0),
                             JetEtaCut = cms.double(5.2)
                             )                                                                   
 

