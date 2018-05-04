select name1, total_severity_this_period, total_severity_previous_period from
(select symptom.name as name1, avg(observation.severity) as total_severity_this_period
from symptom,observation
where symptom.symptom_id = observation.symptom_id
and observation.patient_id = ?
and observation.symptom_start_time >= ?
and observation.symptom_start_time <= ?
group by symptom.name) inner join
(select symptom.name as name2, avg(observation.severity) as total_severity_previous_period
from symptom, observation
where symptom.symptom_id = observation.symptom_id
and observation.patient_id = ?
and observation.symptom_start_time >= date(date(?), '-' || (julianday(date(?)) - julianday(date(?)) + 1) || ' days')
and observation.symptom_start_time <= date(date(?), '-1 days')
group by symptom.name) on name1 = name2;