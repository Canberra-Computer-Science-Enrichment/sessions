(define (domain blocksworld-ground)

  (:predicates (AisTopMost) (BisTopMost) (CisTopMost) (DisTopMost) (EisTopMost)
               (AonB) (AonC) (AonD) (AonE)
               (BonA) (BonC) (BonD) (AonE)
               (ConA) (ConB) (ConD) (ConE)
               (DonA) (DonB) (DonC) (ConE)
               (EonA) (EonB) (EonC) (EonD)
               (AonTable) (BonTable) (ConTable) (DonTable) (EonTable)
               (holdingA) (holdingB) (holdingC) (holdingD) (holdingE)
               (gripperFree)
  )



  ;; take a block from table

  (:action take-A-from-table
           :precondition (and (gripperFree) (AonTable) (AisTopMost))
           :effect (and (holdingA) 
                        (not (gripperFree))
                        (not (AonTable))
                        (not (AisTopMost))))

  (:action take-B-from-table
           :precondition (and (gripperFree) (BonTable) (BisTopMost))
           :effect (and (holdingB)
                        (not (gripperFree))
                        (not (BonTable))
                        (not (BisTopMost))))

  (:action take-C-from-table
           :precondition (and (gripperFree) (ConTable) (CisTopMost))
           :effect (and (holdingC)
                        (not (gripperFree))
                        (not (ConTable))
                        (not (CisTopMost))))

  (:action take-D-from-table
           :precondition (and (gripperFree) (DonTable) (DisTopMost))
           :effect (and (holdingD) 
                        (not (gripperFree))
                        (not (DonTable))
                        (not (DisTopMost))))

  (:action take-E-from-table
           :precondition (and (gripperFree) (EonTable) (EisTopMost))
           :effect (and (holdingE)
                        (not (gripperFree))
                        (not (EonTable))
                        (not (EisTopMost))))




  ;; place a block on table

  (:action place-A-on-table
           :precondition (and (holdingA))
           :effect (and (not (holdingA))
                        (gripperFree)
                        (AonTable)
                        (AisTopMost)))

  (:action place-B-on-table
           :precondition (and (holdingB))
           :effect (and (not (holdingB))
                        (gripperFree)
                        (BonTable)
                        (BisTopMost)))

  (:action place-C-on-table
           :precondition (and (holdingC))
           :effect (and (not (holdingC))
                        (gripperFree)
                        (ConTable)
                        (CisTopMost)))

  (:action place-D-on-table
           :precondition (and (holdingD))
           :effect (and (not (holdingD))
                        (gripperFree)
                        (DonTable)
                        (DisTopMost)))

  (:action place-E-on-table
           :precondition (and (holdingE))
           :effect (and (not (holdingE))
                        (gripperFree)
                        (EonTable)
                        (EisTopMost)))



  ;; place a block on a tower

  ;; Just for our exercise: The list of available state variables:
  ;;
  ;; (AisTopMost) (BisTopMost) (CisTopMost) (DisTopMost) (EisTopMost)
  ;; (AonB) (AonC) (AonD) (AonE) (BonA) (BonC) (BonD) (AonE)
  ;; (ConA) (ConB) (ConD) (ConE) (DonA) (DonB) (DonC) (ConE)
  ;; (EonA) (EonB) (EonC) (EonD)
  ;; (AonTable) (BonTable) (ConTable) (DonTable) (EonTable)
  ;; (holdingA) (holdingB) (holdingC) (holdingD) (holdingE)
  ;; (gripperFree)
  ;;

  ;; EXERCISE 1:

  ;; complete this stack-A-onto-B action using the available state variables
  
  (:action stack-A-onto-B
           :precondition (and ... )
           :effect (and ...)
  )

  (:action stack-A-onto-C
           :precondition (and ... )
           :effect (and ...)
  )
  
  (:action stack-A-onto-D
           :precondition (and ... )
           :effect (and ...)
  )
  
  (:action stack-A-onto-E
           :precondition (and ... )
           :effect (and ...)
  )
 
  ;; other stack actions are still missing!
  ;; i.e, stack-B-onto-A, stack-B-onto-C, stack-B-onto-D, stack-B-onto-E
  ;;      stack-C-onto-A, stack-C-onto-B, stack-C-onto-D, stack-C-onto-E
  ;;      stack-D-onto-A, stack-D-onto-B, stack-D-onto-C, stack-B-onto-E  
  ;;      stack-E-onto-A, stack-E-onto-B, stack-E-onto-C, stack-E-onto-D  
  
  
  
  
  
  ;; take a block from a tower

  ;; Just for our exercise: The list of available state variables:
  ;;
  ;; (AisTopMost) (BisTopMost) (CisTopMost) (DisTopMost) (EisTopMost)
  ;; (AonB) (AonC) (AonD) (AonE) (BonA) (BonC) (BonD) (AonE)
  ;; (ConA) (ConB) (ConD) (ConE) (DonA) (DonB) (DonC) (ConE)
  ;; (EonA) (EonB) (EonC) (EonD)
  ;; (AonTable) (BonTable) (ConTable) (DonTable) (EonTable)
  ;; (holdingA) (holdingB) (holdingC) (holdingD) (holdingE)
  ;; (gripperFree)
  ;;

  ;; EXERCISE 2:

  ;; complete this unstack-A-from-B action using the available state variables
  
  (:action unstack-A-from-B
           :precondition (and ... )
           :effect (and ...)
  )
           
  ;; other unstack actions are still missing!
  ;; i.e., untack A from all other blocks B, C, D, and E
  ;;       and the same for unstacking all other possible top-most blocks B to E
           
)
