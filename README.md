# postcodes
Library to parse postal code format





### Command line script
You can use command line created on pip install process to validate postcodes

#### Validating postcode on command line in text output
```
postcodes -p 'A9A 9AA'                           
Parsing postcode validations...

---
Postcode (A9A 9AA) format is: VALID
  Attributes:
    -> area: A 
    -> district: 9A 
    -> sector: 9 
    -> unit: AA 

---
Results:
  -> Valid postcodes: (A9A 9AA)
```
**Exit code**: 0

```
$postcodes -p 'AA9A 9AAA' 'A9A 9AA' 'A9 9AA' 'AA9A 9' 'AA9 A9' 
Parsing postcode validations...

---
Postcode (AA9A 9AAA) format is: INVALID
  Errors:
    -> Invalid unit format.
  Attributes:
    -> area: AA 
    -> district: 9A 
    -> sector: 9 
    -> unit: AAA (invalid format)

---
Postcode (A9A 9AA) format is: VALID
  Attributes:
    -> area: A 
    -> district: 9A 
    -> sector: 9 
    -> unit: AA 

---
Postcode (A9 9AA) format is: VALID
  Attributes:
    -> area: A 
    -> district: 9 
    -> sector: 9 
    -> unit: AA 

---
Postcode (AA9A 9) format is: INVALID
  Errors:
    -> Invalid unit format.
  Attributes:
    -> area: AA 
    -> district: 9A 
    -> sector: 9 
    -> unit:  (invalid format)

---
Postcode (AA9 A9) format is: INVALID
  Errors:
    -> Invalid sector format.
    -> Invalid unit format.
  Attributes:
    -> area: AA 
    -> district: 9 
    -> sector:  (invalid format)
    -> unit: A9 (invalid format)

---
Results:
  -> Valid postcodes: (A9A 9AA), (A9 9AA)
  -> Invalid postcodes: (AA9A 9AAA), (AA9A 9), (AA9 A9)
```

**Exit code**: 1