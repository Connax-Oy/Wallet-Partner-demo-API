## Get serial number by token
### Method
POST
### Route
`/` (request to root)
### Request body
- `action`: string, value is always `"get"`
- `token`: string

### Responses
<table>
<tbody>
<tr>
<td>Code</td><td>Description</td><td>Example value</td>
</tr><tr>
<td> 200 </td>
<td> Success </td>
<td> <pre>
{
    "status": "success",
    "code": 200,
    "payload": {
        "data": {
            "primaryFields": [
                {
                    "changeMessage": "New card %@",
                    "key": "serialnumber",
                    "label": "Serial number",
                    "value": {{serial_number}}
                }
            ]
        }
    },
    "serial_number": {{serial_number}}
}
</pre> </td>
</tr><tr>
<td> 200 </td>
<td> Failure: serial number not found </td>
<td> <pre>
{
    "status": "error",
    "code": 404
}
</pre> </td>
</tr>
</tbody>
</table>