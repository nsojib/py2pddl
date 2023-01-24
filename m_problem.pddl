(define
	(problem medicine)
	(:domain medicine)
	(:objects
		kitchen couch home - landmark
		nathan - person
		pioneer - robot
	)
	(:init 
		(robot_at pioneer home) 
		(medicine_location kitchen) 
		(unknown (person_at nathan couch) )
		(unknown (person_at nathan kitchen) ) 
		(unknown (person_at nathan home) )
		(oneof (person_at nathan couch) (person_at nathan kitchen) (person_at nathan home))	
		(unknown (guide_to_succeeded_attempt_1) )
		(unknown (guide_to_succeeded_attempt_2) ) 
		(unknown (notify_automated_succeeded) )
		(unknown (notify_recorded_succeeded) )
	)
	(:goal (success))
)
