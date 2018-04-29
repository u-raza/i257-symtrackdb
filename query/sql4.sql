select s.Name, o.symptom_start_time, o.severity, 'current_period' as period from patient p 
left outer join observation o
on o.patient_id = o.patient_id
left outer join symptom s
on s.symptom_id = o.symptom_id
where p.patient_id = ?
and o.symptom_start_time >= ?
and o.symptom_start_time <= ?
group by s.Name, o.symptom_start_time, o.severity
union all
select s.Name, o.symptom_start_time, o.severity, 'previous_period' as period from patient p
left outer join observation o
on o.patient_id = o.patient_id
left outer join symptom s
on s.symptom_id = o.symptom_id
where p.patient_id = ?
and o.symptom_start_time >= date(date(?), '-' || (julianday(date(?)) - julianday(date(?)) + 1) || ' days')
and o.symptom_start_time <= date(date(?), '-1 days')
group by s.Name, o.symptom_start_time, o.severity;