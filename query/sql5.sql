select observation.symptom_start_time, sum(observation.severity) as total_severity
from symptom,observation
where symptom.symptom_id = observation.symptom_id
and observation.patient_id = 1
and observation.symptom_start_time >= '2016-09-13'
and observation.symptom_start_time <= '2016-09-14'
group by observation.symptom_start_time;