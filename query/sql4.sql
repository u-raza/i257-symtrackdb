select symptom.name, observation.symptom_start_time, observation.severity, 'current_period' as period
from symptom,observation
where symptom.symptom_id = observation.symptom_id
and observation.patient_id = 1
and observation.symptom_start_time >= '2016-09-13'
and observation.symptom_start_time <= '2016-09-14'
group by symptom.name, observation.symptom_start_time, observation.severity
union all
select symptom.Name, observation.symptom_start_time, observation.severity, 'previous_period' as period
from symptom, observation
where symptom.symptom_id = observation.symptom_id
and observation.patient_id = 1
and observation.symptom_start_time >= date(date('2016-09-13'), '-' || (julianday(date('2016-09-14')) - julianday(date('2016-09-13')) + 1) || ' days')
and observation.symptom_start_time <= date(date('2016-09-13'), '-1 days')
group by symptom.name, observation.symptom_start_time, observation.severity