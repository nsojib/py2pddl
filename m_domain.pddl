(define
	(domain medicine)
	(:requirements :strips :typing)
	(:types
		landmark
		person
		robot
	)
	(:predicates
		(asked_caregiver_help ?p - person)
		(enable_check_guide_1 )
		(enable_check_guide_2 )
		(guide_to_succeeded_attempt_1 )
		(guide_to_succeeded_attempt_2 )
		(init_guide_person_to_landmark_attempt )
		(init_move_to_landmark )
		(medicine_location ?loc - landmark)
		(notify_automated_succeeded )
		(notify_recorded_succeeded )
		(person_at ?p - person ?loc - landmark)
		(robot_at ?r - robot ?loc - landmark)
		(robot_updated_1 )
		(robot_updated_2 )
		(success )
		(tried_guide_person_landmark_1 )
		(tried_guide_person_landmark_2 )
	)
	(:action InitguidePersonToLandmarkAttempt
		:parameters (?r - robot ?p - person ?to - landmark)
		:precondition  ( and 
				(robot_at ?r ?to)
				(person_at ?p ?to)
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		 :effect (and
			      (forall (?loc - landmark)
				    (not (robot_at ?r ?loc))
			      )
			      (init_guide_person_to_landmark_attempt)
	  	        )

	)
	(:action UpdatePersonLoc1
		:parameters (?p - person ?from - landmark ?to - landmark)
		:precondition  ( and 
				(guide_to_succeeded_attempt_1 )
				(person_at ?p ?from)
				(medicine_location ?to)
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		:effect  ( and 
				(not (person_at ?p ?from))
				(person_at ?p ?to)
			)
	)
	(:action UpdatePersonLoc2
		:parameters (?p - person ?from - landmark ?to - landmark)
		:precondition  ( and 
				(guide_to_succeeded_attempt_2 )
				(person_at ?p ?from)
				(medicine_location ?to)
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		:effect  ( and 
				(not (person_at ?p ?from))
				(person_at ?p ?to)
			)
	)
	(:action UpdateSuccess1
		:parameters ()
		:precondition  ( and 
				(notify_automated_succeeded )
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		:effect (success )

	)
	(:action UpdateSuccess2
		:parameters ()
		:precondition  ( and 
				(notify_recorded_succeeded )
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		:effect (success )

	)
	(:action UpdateSuccess3
		:parameters (?p - person)
		:precondition  ( and 
				(asked_caregiver_help ?p)
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		:effect (success )

	)
	(:action askCaregiverHelpMedicine1
		:parameters (?r - robot ?p - person ?loc - landmark)
		:precondition  ( and 
				(not (notify_automated_succeeded ))
				(not (notify_recorded_succeeded ))
				(robot_at ?r ?loc)
				(person_at ?p ?loc)
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		:effect (asked_caregiver_help ?p)

	)
	(:action askCaregiverHelpMedicine2
		:parameters (?r - robot ?p - person ?loc - landmark)
		:precondition  ( and 
				(not (guide_to_succeeded_attempt_1 ))
				(not (guide_to_succeeded_attempt_2 ))
				(robot_at ?r ?loc)
				(person_at ?p ?loc)
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		:effect (asked_caregiver_help ?p)

	)
	(:action checkGuideToSucceeded1
		:parameters (?loc - landmark)
		:precondition  ( and 
				(tried_guide_person_landmark_1 )
				(enable_check_guide_1 )
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		:observe (guide_to_succeeded_attempt_1 )
	)
	(:action checkGuideToSucceeded2
		:parameters (?loc - landmark)
		:precondition  ( and 
				(tried_guide_person_landmark_2 )
				(enable_check_guide_2 )
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		:observe (guide_to_succeeded_attempt_2 )
	)
	(:action detectPerson
		:parameters (?r - robot ?p - person ?loc - landmark)
		:precondition  ( and 
				(robot_at ?r ?loc)
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		:observe (person_at ?p ?loc)
	)
	(:action guidePersonToLandmarkAttempt1
		:parameters (?r - robot ?p - person ?to - landmark)
		:precondition  ( and 
				(not (tried_guide_person_landmark_1 ))
				(medicine_location ?to)
				(not (init_move_to_landmark ))
				(init_guide_person_to_landmark_attempt )
			)
		:effect  ( and 
				(robot_at ?r ?to)
				(tried_guide_person_landmark_1 )
				(enable_check_guide_1 )
				(not (init_guide_person_to_landmark_attempt ))
			)
	)
	(:action guidePersonToLandmarkAttempt2
		:parameters (?r - robot ?p - person ?to - landmark)
		:precondition  ( and 
				(tried_guide_person_landmark_1 )
				(not (tried_guide_person_landmark_2 ))
				(medicine_location ?to)
				(not (init_move_to_landmark ))
				(init_guide_person_to_landmark_attempt )
			)
		:effect  ( and 
				(robot_at ?r ?to)
				(tried_guide_person_landmark_2 )
				(enable_check_guide_2 )
				(not (init_guide_person_to_landmark_attempt ))
			)
	)
	(:action initMoveToLandmark
		:parameters (?r - robot)
		:precondition  ( and 
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		 :effect (and
			      (forall (?loc - landmark)
				  (not (robot_at ?r ?loc))
			      )
			      (init_move_to_landmark)
	  	        )

	)
	(:action moveToLandmark
		:parameters (?r - robot ?to - landmark)
		:precondition  ( and 
				(init_move_to_landmark )
				(not (init_guide_person_to_landmark_attempt ))
			)
		:effect  ( and 
				(robot_at ?r ?to)
				(not (enable_check_guide_1 ))
				(not (enable_check_guide_2 ))
				(not (init_move_to_landmark ))
			)
	)
	(:action notifyAutomatedMedicineAt
		:parameters (?r - robot ?p - person ?loc - landmark)
		:precondition  ( and 
				(robot_at ?r ?loc)
				(person_at ?p ?loc)
				(medicine_location ?loc)
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		:observe (notify_automated_succeeded )
	)
	(:action notifyRecordedMedicineAt
		:parameters (?r - robot ?p - person ?loc - landmark)
		:precondition  ( and 
				(not (notify_automated_succeeded ))
				(robot_at ?r ?loc)
				(person_at ?p ?loc)
				(medicine_location ?loc)
				(not (init_move_to_landmark ))
				(not (init_guide_person_to_landmark_attempt ))
			)
		:observe (notify_recorded_succeeded )
	)
)
