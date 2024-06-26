Example of swagger documentation separating by router tags.

Imagine you have 2 big API parts - admin related and site related endpoints. Your goal is
get this endpoints in two separate swaggers. All you need is add tags to routers, create a 
new route (for example "/docs/site") and generate a new openapi spec.