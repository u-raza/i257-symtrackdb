select s1.name, s1. total_severity_this_period, s2. total_severity_previous_period from
(select s.Name, avg(o.severity) as total_severity_this_period  from patient p 
left outer join observation o
on o.patient_id = o.patient_id
left outer join symptom s
on s.symptom_id = o.symptom_id
where p.patient_id = ?
and o.symptom_start_time >= ?
and o.symptom_start_time <= ?
group by s.symptom_id) s1
inner join
(select s.Name, avg(o.severity) as total_severity_previous_period  from patient p
left outer join observation o
on o.patient_id = o.patient_id
left outer join symptom s
on s.symptom_id = o.symptom_id
where p.patient_id = ?
and o.symptom_start_time >= date(date(?), '-' || (julianday(date(?)) - julianday(date(?)) + 1) || ' days')
and o.symptom_start_time <= date(date(?), '-1 days')
group by s.symptom_id) s2
on s1.name = s2.name