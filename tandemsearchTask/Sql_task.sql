Select
    i.id AS InvoiceId,
    i.BillingDate,
    c.Name AS CustomerName,
    rb.Name AS ReferrerName
from
    invoices i
left join
    customers c ON c.id = i.CustomerId
left join
    customers rb ON rb.id = c.RefferdBy
order by 
    i.BillingDate;