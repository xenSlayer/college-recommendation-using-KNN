# controller
from django.shortcuts import render

from knn import RecommendationUsingKNN


def index(request):
    # return template when user open the following url
    # [Template] : index.html
    # [URL] : /index
    return render(request, 'index.html', {})


def recommendation(request):
    # return template when user open the following url
    # [Template] : recommendation.html
    # [URL] : /recommendation

    # extracting fee data from url query param
    fee = int(request.GET.get('fee'))
    # extracting percentage data from url query param
    percentage = float(request.GET.get('percentage'))
    # extracting rating data from url query param
    rating = float(request.GET.get('rating'))
    '''
        RecommendationUsingKNN
            params:
                [fee] : coellge fee
                [percentage] : average percentage
                [rating] : average rating     
    '''
    colleges = RecommendationUsingKNN(
        fee=fee, percentage=percentage, rating=rating)
    # render django template with recommended college list, user entered fee, user entered percentage and user entered rating
    return render(request, 'recommendation.html', {"colleges": colleges, "fee": fee,
                                                   "percentage": percentage, "rating": rating})
