select symptom.name, avg(observation.severity) as average_severity
from observation, symptom
where observation.symptom_id = symptom.symptom_id
and observation.patient_id = ?
and observation.symptom_start_time >= ?
and observation.symptom_start_time <= ?
group by symptom.name;