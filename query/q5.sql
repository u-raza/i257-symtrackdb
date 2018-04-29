select o.symptom_start_time, sum(o.severity) as total_severity  from patient p 
left outer join observation o
on o.patient_id = o.patient_id
left outer join symptom s
on s.symptom_id = o.symptom_id
where p.patient_id = ?
and o.symptom_start_time >= ?
and o.symptom_start_time <= ?
group by o.symptom_start_time;