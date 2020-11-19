(define (problem blocksworld-prob1)

  (:domain blocksworld-lifted)
  
  (:objects A B C D E - block)
  
  (:init (topMost A) (on A B) (on B C) (onTable C)
         (topMost D) (on D E) (onTable E)
         (gripperFree)
  )
  
  (:goal (and (topMost A) (on A D) (on D C) (onTable C)
              (topMost E) (on E B) (onTable B))
  )
)
