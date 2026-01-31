from django.shortcuts import render,redirect

from django.views import View

from .models import Package,MentorChoices,DestinationTypeChoices,PackageChoices

from .forms import PackageForm

from django.db.models import Q
# Create your models here.

class HomeView(View):

    template = 'home.html'

    def get(self,request,*args,**kwargs):

        data = {'page':'Home'}

        return render(request,self.template,context=data)
    

class AboutView(View):

    template = 'about/about.html'

    def get(self,request,*args,**kwargs):

        data = {'page':'About Us'}

        return render(request,self.template,context=data)
    

class contactView(View):

    template = 'contact/contact.html'

    def get(self,request,*args,**kwargs):

        data = {'page':'Contact Us'}

        return render(request,self.template,context=data)
    
    
class ServiceView(View):

    template = 'services/services.html'

    def get(self,request,*args,**kwargs):

        data = {'page':'services'}

        return render(request,self.template,context=data)



class PackageListView(View):

    template= 'packages/package_list.html'

    def get(self,request,*args,**kwargs):

        query = request.GET.get('query')

        packages = Package.objects.filter(active_status=True)

        if query:

            packages = packages.filter(Q(name__icontains=query,)|
                                       Q(description__icontains=query,)|
                                       Q(destination_type__icontains=query,)
                                       ).distinct()

        data = {'page':'Packages','packages':packages,'query':query}

        return render(request,self.template,context=data)
    

# class PackageCreateView(View):

#     def get(self,request,*args,**kwargs):

#         data = {'page':'Create Package'}

#         return render(request,'packages/package_create.html',context=data)
    
#     def post(self,request,*args,**kwargs):

#         package_data = request.POST

#         name = package_data.get('name')

#         photo = request.FILES.get('photo')

#         description = package_data.get('description')

#         start_date = package_data.get('start_date')

#         destination_type = package_data.get('destination')

#         duration = package_data.get('duration')

#         package_type = package_data.get('package_type')

#         mentor = package_data.getlist('mentor')

#         price = package_data.get('price')

#         return redirect('package-list')




class PackageCreateView(View):

    form_class = PackageForm

    template = 'packages/package_create.html'
    
    def get(self,request,*args,**kwargs):

        form = self.form_class()

        data = {'page':'Create Package','form':form}

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):     

        form = self.form_class(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect('package-list')
    
        data = {'page':'Create Package','form':form}

        return render(request,self.template,context=data)

class PackageDetailsView(View):

    template = 'packages/package-details.html'

    def get(self,request,*args,**kwargs):

        uuid =  kwargs.get('uuid')

        package = Package.objects.get(uuid=uuid)

        # recommended_packages = get_recommended_packages(package)

        data = {'package':package,'page':package.name}
        
        return render(request,self.template,context=data)


#  @method_decorator(permitted_user_roles(['Admin']),name='dispatch')  
#  
class PackageEditView(View):

    form_class = PackageForm

    template = 'packages/package-edit.html'

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        package = Package.objects.get(uuid=uuid)

        form = self.form_class(instance=package)

        data = {'form':form,'page':package.name}

        return render(request,self.template,context=data)

    def post(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        package = Package.objects.get(uuid=uuid)

        form = self.form_class(request.POST,request.FILES,instance=package)

        if form.is_valid():

            form.save()

            return redirect('package-details',uuid=uuid)
        
        data = {'form':form,'page':package.name}

        return render(request,self.template,context=data)



class PackageDeleteView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        package = Package.objects.get(uuid=uuid)

        # hard delete
        # package.delete()

        package.active_status = False

        package.save()

        package.success(request,'package deleted succesfully')

        return redirect('package-list')