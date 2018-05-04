select symptom.name, avg(observation.severity) as average_severity
from observation, symptom
where observation.symptom_id = symptom.symptom_id
and observation.patient_id = 2
and observation.symptom_start_time >= '2016-09-13'
and observation.symptom_start_time <= '2016-09-14'
group by symptom.name;