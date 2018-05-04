select sum(average_severity) as total_severity from
(select symptom.name, avg(observation.severity) as average_severity
from symptom, observation
where symptom.symptom_id = observation.symptom_id
and observation.patient_id = 1
and observation.symptom_start_time >= '2016-09-13'
and observation.symptom_start_time <= '2016-09-14'
group by symptom.name);