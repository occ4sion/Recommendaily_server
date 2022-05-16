from django.http import HttpResponse
 
def send(request, user): ## post a batch
    output = ''
    if request.GET:
        output = "<h2>Go away</h2>"
    if request.POST:
        output = "<h2>Thanks for data</h2>"
    return HttpResponse(output)
 
def recieve(request, user): ## get a game ID's by userID
    items = int(request.GET.get("item", -1)) * 10
    output = f"<h2>For user {user}</h2><h3>items: {items}</h3>"
    return HttpResponse(output)