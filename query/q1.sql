select sum(average_severity) as total_severity from
(select symptom.name, avg(observation.severity) as average_severity
from symptom, observation
where symptom.symptom_id = observation.symptom_id
and observation.patient_id = ?
and observation.symptom_start_time >= ?
and observation.symptom_start_time <= ?
group by symptom.name);