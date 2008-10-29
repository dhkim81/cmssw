import FWCore.ParameterSet.Config as cms

trackingTruthValid = cms.EDFilter("TrackingTruthValid",
    #to run on original collection
    #   InputTag src = trackingtruthprod:
    #   string outputFile = "trackingtruthhisto.root" 
    #to run on merged collection (default)
    src = cms.InputTag("mergedtruth","MergedTrackTruth"),
    outputFile = cms.string('')
)


