-- MongoDB Sort Ages
-- Your collection: Collection_C794G

-- MongoDB version: 4.4.8

-- Your query should return only the fields FirstName, LastName, and Age from your collection where LastName = Smith or FirstName = Robert 
-- and the documents should be sorted by Age in ascending order. 
-- Your query will be excuted via the runCommand function.


-- [
--   {
--     "_id": {
--       "$oid": "64ad59df568b575f590cc588"
--     },
--     "FirstName": "Daniel",
--     "LastName": "Smith",
--     "Age": 25
--   },
--   {
--     "_id": {
--       "$oid": "64ad59df568b575f590cc589"
--     },
--     "FirstName": "Mike",
--     "LastName": "Smith",
--     "Age": 22
--   },
--   {
--     "_id": {
--       "$oid": "64ad59df568b575f590cc58a"
--     },
--     "FirstName": "Jenny",
--     "LastName": "Richards",
--     "Age": 28
--   },
--   {
--     "_id": {
--       "$oid": "64ad59df568b575f590cc58b"
--     },
--     "FirstName": "Robert",
--     "LastName": "Black",
--     "Age": 22
--   },
--   {
--     "_id": {
--       "$oid": "64ad59df568b575f590cc58c"
--     },
--     "FirstName": "Noah",
--     "LastName": "Fritz",
--     "Age": 30
--   },
--   {
--     "_id": {
--       "$oid": "64ad59df568b575f590cc58d"
--     },
--     "FirstName": "Ashley",
--     "LastName": "Johnson",
--     "Age": 25
--   }
-- ]


{
  "find": "Collection_B285X",
  "filter": {
    "$or": [
      { "LastName": "Smith" },
      { "FirstName": "Robert" }
    ]
  },
  "projection": { "FirstName": 1, "LastName": 1, "Age": 1, "_id": 0 },
  "sort": { "Age": 1 }
}