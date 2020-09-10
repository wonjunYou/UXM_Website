from django.shortcuts import render

# Create your views here.
def publication(request): 
    journal_paper_list = [{
        "title":"논문 제목1",
        "author":"논문 저자1",
        "publication_data":"어디어디학술지 몇년 몇월 몇일"},
        {
        "title":"논문 제목2", 
        "author":"논문 저자2",
        "publication_data":"어디어디학술지 몇년 몇월 몇일"
        },
        {
        "title":"논문 제목3", 
        "author":"논문 저자3",
        "publication_data":"어디어디학술지 몇년 몇월 몇일"}]
    conference_paper_list = [{
        "title":"논문 제목4",
        "author":"논문 저자4",
        "publication_data":"어디어디학술지 몇년 몇월 몇일"},
        {
        "title":"논문 제목5", 
        "author":"논문 저자5",
        "publication_data":"어디어디학술지 몇년 몇월 몇일"
        },
        {
        "title":"논문 제목6", 
        "author":"논문 저자6",
        "publication_data":"어디어디학술지 몇년 몇월 몇일"}]
    return render(request, 'publication.html', {"journal_paper_list":journal_paper_list, "conference_paper_list":conference_paper_list})
    
def main(request):
    return render(request, 'main.html')