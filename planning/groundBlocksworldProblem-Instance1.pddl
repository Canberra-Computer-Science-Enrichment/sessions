(define (problem blocksworld-prob1)

  (:domain blocksworld-ground)
  
  (:init (AisTopMost) (AonB) (BonC) (ConTable)
         (DisTopMost) (DonE) (EonTable)
         (gripperFree)
  )
  
  (:goal (and (AisTopMost) (AonD) (DonC) (ConTable)
              (EisTopMost) (EonB) (BonTable))
  )
)
