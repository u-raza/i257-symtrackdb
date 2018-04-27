select s.Name, o.symptom_start_time, o.severity, 'current_period' as period from patient p 
left outer join observation o
on o.patient_id = o.patient_id
left outer join symptom s
on s.symptom_id = o.symptom_id
where p.patient_id = 7
and o.symptom_start_time >= '2016-09-13'
and o.symptom_start_time <= '2016-09-14'
group by s.Name, o.symptom_start_time, o.severity
union all

select s.Name, o.symptom_start_time, o.severity, 'previous_period' as period from patient p 
left outer join observation o
on o.patient_id = o.patient_id
left outer join symptom s
on s.symptom_id = o.symptom_id
where p.patient_id = 7
and o.symptom_start_time >= date(date('2016-09-13'), '-' || (julianday(date('2016-09-14')) - julianday(date('2016-09-13')) + 1) || ' days')
and o.symptom_start_time <= date(date('2016-09-13'), '-1 days')
group by s.Name, o.symptom_start_time, o.severity