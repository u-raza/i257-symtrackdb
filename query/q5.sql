select observation.symptom_start_time, sum(observation.severity) as total_severity
from symptom,observation
where symptom.symptom_id = observation.symptom_id
and observation.patient_id = ?
and observation.symptom_start_time >= ?
and observation.symptom_start_time <= ?
group by observation.symptom_start_time;