-- MongoDB FindModify
-- Your collection: Collection_CGPK3

-- MongoDB version: 4.4.8

-- Your query should perform a findAndModify operation on your collection and return the modified document. 
-- Find the document where the Age = 30 and then add a field called canRent 
-- and set its value to true. Your query will be excuted via the runCommand function.


-- [
--   {
--     "_id": {
--       "$oid": "64ad5a608f951bbf010cc8a2"
--     },
--     "FirstName": "Daniel",
--     "LastName": "Smith",
--     "Age": 25
--   },
--   {
--     "_id": {
--       "$oid": "64ad5a608f951bbf010cc8a3"
--     },
--     "FirstName": "Mike",
--     "LastName": "Smith",
--     "Age": 22
--   },
--   {
--     "_id": {
--       "$oid": "64ad5a608f951bbf010cc8a4"
--     },
--     "FirstName": "Jenny",
--     "LastName": "Richards",
--     "Age": 28
--   },
--   {
--     "_id": {
--       "$oid": "64ad5a608f951bbf010cc8a5"
--     },
--     "FirstName": "Robert",
--     "LastName": "Black",
--     "Age": 22
--   },
--   {
--     "_id": {
--       "$oid": "64ad5a608f951bbf010cc8a6"
--     },
--     "FirstName": "Noah",
--     "LastName": "Fritz",
--     "Age": 30
--   },
--   {
--     "_id": {
--       "$oid": "64ad5a608f951bbf010cc8a7"
--     },
--     "FirstName": "Ashley",
--     "LastName": "Johnson",
--     "Age": 25
--   }
-- ]

-- [
--   {
--     "lastErrorObject": {
--       "n": 1,
--       "updatedExisting": true
--     },
--     "value": {
--       "_id": {
--         "$oid": "64ad5a608f951bbf010cc8a6"
--       },
--       "FirstName": "Noah",
--       "LastName": "Fritz",
--       "Age": 30,
--       "canRent": true
--     },
--     "ok": 1,
--     "$clusterTime": {
--       "clusterTime": {
--         "$timestamp": {
--           "t": 1689082531,
--           "i": 9
--         }
--       },
--       "signature": {
--         "hash": {
--           "$binary": "1nlvr+ldJHOyA7dOzWV21UAeIAs=",
--           "$type": "00"
--         },
--         "keyId": 7215678038057419000
--       }
--     },
--     "operationTime": {
--       "$timestamp": {
--         "t": 1689082531,
--         "i": 9
--       }
--     }
--   }
-- ]


{
  "findAndModify": "Collection_CGPK3",
  "query": { "Age": 30 },
  "update": { "$set": { "canRent": true } },
  "new": true
}
