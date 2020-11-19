(define (domain blocksworld-lifted)

  (:types block)

  (:predicates (topMost ?b - block)
               (on ?b1 ?b2 - block)
               (onTable ?b - block)
               (holding ?b - block)
               (gripperFree)
  )

  ;; take a block from table

  (:action take-from-table
           :parameters (?b - block)
           :precondition (and (gripperFree) (onTable ?b) (topMost ?b))
           :effect (and (not (gripperFree))
                        (holding ?b)
                        (not (onTable ?b))
                        (not (topMost ?b))))

  ;; place a block on table

  (:action place-on-table
           :parameters (?b - block)
           :precondition (and (holding ?b))
           :effect (and (not (holding ?b))
                        (gripperFree)
                        (onTable ?b)
                        (topMost ?b)))

  ;; place a block on a tower

  (:action stack
           :parameters (?b1 ?b2 - block)
           :precondition (and (holding ?b1) (topMost ?b2))
           :effect (and (on ?b1 ?b2) (topMost ?b1) 
                        (gripperFree)
                        (not (holding ?b1))
                        (not (topMost ?b2))))

  ;; take a block from a tower


  ;; Just for our exercise: The list of available state variables:
  ;;
  ;; (topMost ?b - block) (on ?b1 ?b2 - block) (onTable ?b - block)
  ;; (holding ?b - block) (gripperFree)
  ;;

  ;; EXERCISE 3:

  ;; complete this unstack action using the available state variables

  (:action unstack
           :parameters (...)
           :precondition (and ...)
           :effect (and ...)
  )

)