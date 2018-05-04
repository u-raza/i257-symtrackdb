select symptom.name, observation.symptom_start_time, observation.severity, 'current_period' as period
from symptom,observation
where symptom.symptom_id = observation.symptom_id
and observation.patient_id = ?
and observation.symptom_start_time >= ?
and observation.symptom_start_time <= ?
group by symptom.name, observation.symptom_start_time, observation.severity
union all
select symptom.Name, observation.symptom_start_time, observation.severity, 'previous_period' as period
from symptom, observation
where symptom.symptom_id = observation.symptom_id
and observation.patient_id = ?
and observation.symptom_start_time >= date(date(?), '-' || (julianday(date(?)) - julianday(date(?)) + 1) || ' days')
and observation.symptom_start_time <= date(date(?), '-1 days')
group by symptom.name, observation.symptom_start_time, observation.severity