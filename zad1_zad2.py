import datetime

class Article:
    def __init__(self, title, author, description, category, views, comments):
        self.title = title (unique = True)
        self.author = author
        self.description = description
        self.category = category
        self.views = 0
        self.comments = []

    @property
    def title(self): 
        return self.title
    @title.setter
    def title(self, title):
        if not (title.is_unique and title.isalpha() and len(title) < 50):
            raise ValueError ("Invalid form data")
        self.title = title
    
    @property
    def author(self): 
        return self.author
    @author.setter
    def author(self, author): 
        if not (author.isalpha() and len(author) < 100):
            raise ValueError ("Invalid form data")
        self.author = author

    @property
    def description(self): 
        return self.description
    @description.setter
    def description(self, description): 
        if not (len(description) < 300):
            raise ValueError ("Invalid form data")
        self.description = description

    @property
    def category(self): 
        return self.category
    @category.setter
    def category(self, category): 
        if not (len(category) < 20):
            raise ValueError ("Invalid form data")
        self.category = category
    
    @property
    def views(self):
        return self.views
    @views.setter
    def views(self, views):
        self.views = views

    @property
    def comments(self):
        return self.comments
    @comments.setter
    def comments(self, comments):
        self.comments = []
        i = 0   
        while i < len(comments):
            self.comments.append(comments[i])


    def insert_new_comment (self, title, author = 'anonim', *, description):
        if not (len(title) < 50 and author.isalpha() and len(author) < 50 and len(description) < 120):
            raise ValueError("Invalid form data")
        self.comments.append((title, author, description))
    
    def delete_comment_by_title (self, title):
        for c in self.comments:
            if c[0] == title:
                del(c)
    
    def delete_comments_by_author (self, author):
        for c in self.comments:
            if c[1] == author:
                del(c)

    def get_comment_by_title (self, title):
        for c in self.comments:
            if c[0] == title:
                return f'{{ {c[0]} : [ {c[1]}, {c[2]} ]}}'
        return f'No comments titled: {title}'

    def get_comments_by_author (self, author):
        all_coments = []
        for c in self.comments:
            if c[1] == author:
                all_coments.append(c)
        if(len(all_coments) > 0):
            return all_coments
        else:
            return f'No comments by author: {author}'

    def inc_views (self, num = 1):
        self.views = self.views + num

    def __str__(self):
        return f'title: {self.title}, author: {self.author}, description: {self.description}, category: {self.category}, views: {self.views}, number_of_comments: {len(self.comments)}'

#ZADATAK 2
class TechArticle(Article):
    
    def __init__(self, title, author, description, category, views, comments, creation_date, lang):
        super().__init__(title, author, description, "tech", views, comments)        
        self.__creation_date = creation_date
        self.__lang = lang

    @property
    def creation_date(self): 
        return self.__creation_date
    @creation_date.setter
    def creation_date(self, creation_date):
        date_split = creation_date.split("/")
        if date_split[0] < 10:
            date_split[0] = "0" + date_split[0]
        if date_split[1] < 10:
            date_split[1] = "0" + date_split[1]
        creation_date = date_split[0] + "/" + date_split[1] + "/" + date_split[2]
        try:
            datetime.datetime.strftime(creation_date, '%d/%m/%y')
        except ValueError:
            raise ValueError("Invalid date format, should be dd/mm/yyyy")
        self.__creation_date = creation_date

    @property
    def lang(self):
        return self.__lang
    @lang.setter
    def set_lang(self, lang):
        if not (lang == "en" or lang == "rs"):
            raise ValueError("Language must be en/rs")
        self.__lang = lang

    def get_comments_by_term(self, term):
        for c in self.comments:
            if c[0] == term:
                return "{' {c[0]} : [{c[1]}, {c[2]}]'}"
            else:
                return f'No comments titled: {term}'

    def __str__(self):
        return f'{super().__str__}, creation_date: {self.__creation_date}, language: {self.__lang}'