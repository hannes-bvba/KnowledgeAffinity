from django.shortcuts import render
from models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseForbidden, HttpResponseRedirect, Http404
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout
from itertools import chain
from django.contrib.auth.decorators import login_required
# Create your views here.

globalMenu = """<ul id="navze">
    <li><a href="/KAAM/logout">logout</a>
        <div class="clear"></div>
    </li>
</ul>

<div class="clear"></div>
"""

#if logged in as KGE you will also be a specific user
WhoIsKGE = 21


def tools_create_users():
    #name passwd team
    userslist =[["Jan","jan",4,"mail@geilenkotten.com"], \
            ["Jos", "jos", 4,"mail@geilenkotten.com"], \
            ["Jelle", "jelle", 4,"mail@geilenkotten.com"], \
            ["Jose", "jose", 4,"mail@geilenkotten.com"], \
            ["Johny", "johny", 4,"mail@geilenkotten.com"], \
            ["Tom", "tom", 5,"mail@geilenkotten.com"], \
            ["Tim", "tim", 5,"mail@geilenkotten.com"], \
            ["Terry", "terry", 5,"mail@geilenkotten.com"] \
            ]
    print userslist
    for user_index in userslist:

        try:
            print user_index[2]
            team= CompetenceTeam.objects.get(pk = int(user_index[2]))
            print team
            user = TeamMember.objects.create_user(user_index[1], user_index[3], user_index[2], competenceTeam=team)
            user.competenceTeam = team
            #                    user.competenceTeam = team
            user.is_staff = True
            user.groups.add(Group.objects.get(pk=1))
            user.save()
        except Exception as e:
            print "can not create ",user_index, e

import random
def tools_random_affinity_skill():
    teams = CompetenceTeam.objects.filter( id__in=(14,13))
    print teams


    users= TeamMember.objects.filter(competenceTeam__in=teams)
    print users
    SkillUsers = Skill_user.objects.filter(teamMember__in = users)

    print SkillUsers

    for su in SkillUsers:

        skill =  random.randrange(0, 10)
        print skill
        affinity = random.randrange(0, 100)
        if affinity < 80:
            aff=0
        else:
            if affinity < 90:
                aff=1
            else:
                aff=2

        print su, skill,aff
        su.skills = skill
        su.affinity = aff
        su.save()
    return HttpResponseRedirect("/KAAM/matrix")


def dotest(request):
#    tools_create_users()
#    tools_random_affinity_skill()
    return HttpResponseRedirect("/KAAM/matrix")



def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/KAAM/matrix")



def index(request):
    return HttpResponseRedirect("/KAAM/matrix")
#    return HttpResponse("Hello, world. You're at the polls index.")

class valuePair(object):
    def __init__(self,label,value,units,color= "#FFFFFF"):
        self.label = label
        if(type(value) == float):
            self.value=round(value, 3)
        else:
            self.value=value
        self.units= units
        self.color=color


def calculate_color(value):

    startR= 0xFF
    startG= 0xFF
    startB= 0x00

    endR= 0x25
    endG= 0xFF
    endB= 0x0D

    max= 10
    min= 0
    if value >= max:
        colour = str(format(endR, '02x')+format(endG, '02x')+format(endB, '02x'))
        return colour
    if value <= min:
        colour = str(format(startR, '02x')+format(startG, '02x')+format(startB, '02x'))
        return colour

    R = int(startR+ (((endR - startR)/max) * value))


    G = int(startG + (((endG - startG) / max) * value))
    B = int(startB + (((endB - startB) / max) * value))

    print value, R,G,B
    colour = str(format(R, '02x') + format(G, '02x') + format(B, '02x'))
    return colour

@login_required(redirect_field_name='next', login_url='/login/')
def SkillUp(request, skillID):
    if request.user.is_authenticated() == False:
        return HttpResponse("please log in first")

    try:
        LI_user = TeamMember.objects.get(pk=request.user.pk)
    except:

        return HttpResponseRedirect('/KAAM/matrix/')

    abilityAfinity = Skill_user.objects.get(pk= skillID )
    print  abilityAfinity
    print LI_user.pk ,abilityAfinity.teamMember.pk

    if LI_user.pk == abilityAfinity.teamMember.pk:
        abilityAfinity.skillsUp()

#    return HttpResponse("updated "+str(abilityAfinity))
    return HttpResponseRedirect('/KAAM/matrix/')

@login_required(redirect_field_name='next', login_url='/login/')
def SkillDown(request, skillID):
    if request.user.is_authenticated() == False:
        return HttpResponse("please log in first")

    try:
        LI_user = TeamMember.objects.get(pk=request.user.pk)
    except:

        return HttpResponseRedirect('/KAAM/matrix/')

    abilityAfinity = Skill_user.objects.get(pk= skillID )
    print  abilityAfinity
    print LI_user.pk ,abilityAfinity.teamMember.pk

    if LI_user.pk == abilityAfinity.teamMember.pk:
        abilityAfinity.skillsDown()

#    return HttpResponse("updated "+str(abilityAfinity))
    return HttpResponseRedirect('/KAAM/matrix/')


@login_required(redirect_field_name='next', login_url='/login/')
def AffinityDown(request, skillID):
    if request.user.is_authenticated() == False:
        return HttpResponse("please log in first")

    try:
        LI_user = TeamMember.objects.get(pk=request.user.pk)
    except:

        return HttpResponseRedirect('/KAAM/matrix/')

    abilityAfinity = Skill_user.objects.get(pk= skillID )
    print  abilityAfinity
    print LI_user.pk ,abilityAfinity.teamMember.pk

    if LI_user.pk == abilityAfinity.teamMember.pk:
        abilityAfinity.AffinityDown()

#    return HttpResponse("updated "+str(abilityAfinity))
    return HttpResponseRedirect('/KAAM/matrix/')

@login_required(redirect_field_name='next', login_url='/login/')
def AffinityUp(request, skillID):
    if request.user.is_authenticated() == False:
        return HttpResponse("please log in first")

    try:
        LI_user = TeamMember.objects.get(pk=request.user.pk)
    except:

        return HttpResponseRedirect('/KAAM/matrix/')

    abilityAfinity = Skill_user.objects.get(pk= skillID )
    print  abilityAfinity
    print LI_user.pk ,abilityAfinity.teamMember.pk

    if LI_user.pk == abilityAfinity.teamMember.pk:
        abilityAfinity.AffinityUp()

#    return HttpResponse("updated "+str(abilityAfinity))
    return HttpResponseRedirect('/KAAM/matrix/')




@login_required(redirect_field_name='next', login_url='/login/')
def KnowledgeAndAffinityMatrix(request, Allid=0):
    All=int(Allid)
    if request.user.is_authenticated() == False:
        return HttpResponse("please log in first")

    try:
        LI_user = TeamMember.objects.get(pk=request.user.pk)
    except:

        return HttpResponseRedirect('/KAAM/matrix/')

    print LI_user

    team = LI_user.competenceTeam
    menu=globalMenu

    TeamLeadLoggedIn = False
    if team.TeamLead.pk == LI_user.pk:
        TeamLeadLoggedIn= True

    titleHead ="team: " + team.Name + ",  user: " +  str(LI_user)


    dataModCodTable=[]

    if All==1:
        titleHead = "All Teams!   user:" +  str(LI_user)
        dataModCodTable.append([valuePair(" ", "<font size=\"1\"> full team View  <br><a href=\"/KAAM/matrix\"> Click here to see only my team </a></font>", "units", "#CEF6F5")])
    else:
        dataModCodTable.append([valuePair(" ", "<font size=\"1\"> my team View  <br><a href=\"/KAAM/matrix1\"> Click here to see the complete company </a></font>", "units", "#CEF6F5")])

    if TeamLeadLoggedIn and not All==1:
        headerrow =[valuePair(" ", "<font size=\"4\"> Team members: </font><font size=\"1\"> <br><a href=\"/KAAM/createAccount\"> add user </a></font>", "units", "#CEF6F5")]
    else:
        headerrow = [ valuePair(" ", "<font size=\"4\"> Team members:  </font>", "units", "#CEF6F5"), ]
    members = TeamMember.objects.filter(competenceTeam=team)
    if All==1:
        teams = CompetenceTeam.objects.filter(company = team.company )
        for teamindex in teams:
            if team != teamindex:
                print "here", members
                members= list(chain(members , TeamMember.objects.filter(competenceTeam = teamindex)))
    for member in members:
        if member.pk == LI_user.pk:
            headerrow.append( valuePair(" ", "<font size=\"3\"><b><u>" + str(member) + "</b></u></font>", "units","#CEF6F5" ))
        else:
            headerrow.append(valuePair(" ", "<font size=\"2\">" + str(member) + "</font>", "units", "#CEF6F5"))
    if All!=1:
        headerrow.append( valuePair(" ", "<font size=\"2\"> adjust my skills </font>", "units","#CEF6F5" ))
        headerrow.append( valuePair(" ", "<font size=\"2\"> adjust my affinity </font>", "units","#CEF6F5" ))
    if TeamLeadLoggedIn :
        headerrow.append(valuePair(" ", "<font size=\"2\"> Average </font>", "units", "#CEF6F5"))
        headerrow.append(valuePair(" ", "<font size=\"2\"> interested </font>", "units", "#CEF6F5"))
        headerrow.append(valuePair(" ", "<font size=\"2\"> very interested </font>", "units", "#CEF6F5"))

    dataModCodTable.append(headerrow)
    skills = Skill_CT.objects.filter(competenceTeam=team)
    if All==1:
        for teamindex in teams:
            if team != teamindex:
                firstlist = list(skills)
                in_second = list(Skill_CT.objects.filter(competenceTeam = teamindex))
                for it in in_second:
                    found=0
                    for it2 in firstlist:
                        if it.skill == it2.skill:
                            found =1
                        print "herefsd",it,it2
                    if found ==0 :
                        firstlist.append(it)
                        skills=firstlist

    print skills
    print "number of skills", len(skills)
    print "number of users", len(members)

    sum_per_user=[0] * len(members)
    interested_per_user=[0] * len(members)
    very_interested_per_user=[0] * len(members)
    nr_skills= len(skills)

    for skill in skills:
        if TeamLeadLoggedIn and not All==1:
            row=[valuePair(" ", "<font size=\"4\"> "+ str(skill.skill)+"  </font> <br> <font size=\"1\">  <a href=\"/KAAM/removeSkillFromTeam/"+str(skill.pk)+"\"> remove skill </a> </font>", "units", "#CEF6F5")]
        else:
            row=[valuePair(" ", "<font size=\"4\"> "+ str(skill.skill)+"  </font> ", "units", "#CEF6F5")]
        sum=0
        count=0
        intt =0
        veryintt =0
        memberIndex=0
        for member in members:

            try:
                abilityAfinity = Skill_user.objects.filter(teamMember =member ).filter(skill = skill.skill)
                ability = abilityAfinity[0].skills
                affinity = abilityAfinity[0].get_affinity_display()
                if abilityAfinity[0].affinity == 1:
                    intt = intt + 1
                    interested_per_user[memberIndex]= interested_per_user[memberIndex] +1
                if abilityAfinity[0].affinity == 2:
                    veryintt = veryintt + 1
                    very_interested_per_user[memberIndex]= very_interested_per_user[memberIndex]+1


            except Exception as e:
                print e
                ability = "error"
                affinity = "error"

            print "====="
            print ability, member, abilityAfinity.count()

            if abilityAfinity.count() ==0:
                sk_u= Skill_user( skill= skill.skill,teamMember=member, affinity=0,skills=0)
                sk_u.save()
                ability = -1
                affinity = "No affinity"

            if member.pk == LI_user.pk:
                LI_abilityAfinity = abilityAfinity[0]

            count =count+1
            sum=sum + ability
            sum_per_user[memberIndex] = sum_per_user[memberIndex] + ability
            row.append( valuePair(" ", "<font size=\"2\"> Skill:"+str(ability) + "<br>"+str(affinity)+"</font>", "units","#"+ str(calculate_color(ability))))
            memberIndex = memberIndex +1
        if All != 1:
            row.append(valuePair(" ", "<font size=\"5\"> <a href=\"/KAAM/SkillUp/"+str(LI_abilityAfinity.pk)+"\"> + </a>    <a href=\"/KAAM/SkillDown/"+str(LI_abilityAfinity.pk)+"\"> - </a>  </font>", "units", "#FFFFFF"))
            row.append(valuePair(" ", "<font size=\"5\"> <a href=\"/KAAM/AffinityUp/"+str(LI_abilityAfinity.pk)+"\"> + </a>    <a href=\"/KAAM/AffinityDown/"+str(LI_abilityAfinity.pk)+"\"> - </a>  </font>", "units", "#FFFFFF"))
        if TeamLeadLoggedIn:
            average= float(sum)/float(count)
            row.append(valuePair(" ", "<font size=\"2\">"+str(round(average,2))+ " </font>", "units", "#FFFFFF"))
            row.append(valuePair(" ", "<font size=\"2\">"+str(intt)+" </font>", "units", "#FFFFFF"))
            row.append(valuePair(" ", "<font size=\"2\">"+str(veryintt)+" </font>", "units", "#FFFFFF"))
        dataModCodTable.append(row)

    if TeamLeadLoggedIn:
        if All==1:
            extra_cols=3
        else:
            extra_cols=5

        row = [valuePair(" ", "<font size=\"1\"> Average </font>", "units", "#CEF6F5")]
        index = 0

        while index < len(members) + extra_cols:
            if index< len(members):
                try:
                    average2 = float(sum_per_user[index]) / float(nr_skills)
                except:
                    average2=0
                row.append(valuePair(" ", "<font size=\"1\">" +str(round(average2,2))+ " </font>", "units", "#FFFFFF"))
            else:
                row.append(valuePair(" ", "<font size=\"1\"> </font>", "units", "#FFFFFF"))

            index = index + 1
        dataModCodTable.append(row)
        row = [valuePair(" ", "<font size=\"1\"> Interested </font>", "units", "#CEF6F5")]
        index = 0
        while index < len(members) + extra_cols:
            if index< len(members):
                row.append(valuePair(" ", "<font size=\"1\">" +str(interested_per_user[index])+ " </font>", "units", "#FFFFFF"))
            else:
                row.append(valuePair(" ", "<font size=\"1\"> </font>", "units", "#FFFFFF"))
            index = index + 1
        dataModCodTable.append(row)
        row = [valuePair(" ", "<font size=\"1\"> Very interested </font>", "units", "#CEF6F5")]
        index = 0
        while index < len(members) + extra_cols:
            if index< len(members):
                row.append(valuePair(" ", "<font size=\"1\">" +str(very_interested_per_user[index])+ " </font>", "units", "#FFFFFF"))
            else:
                row.append(valuePair(" ", "<font size=\"1\"> </font>", "units", "#FFFFFF"))
            index = index + 1
        dataModCodTable.append(row)

        if not All==1:
            row =[valuePair(" ", "<font size=\"1\"> <a href=\"/KAAM/addSkillToTeam\"> add skill </a></font>", "units", "#FFFFFF")]
            index =0
            while index < len(members) +extra_cols:
                row.append(valuePair(" ",  "<font size=\"1\"> </font>", "units", "#FFFFFF"))
                index =index +1
            dataModCodTable.append(row)


   # print team.teammember_set.all()

    return render_to_response('resource.html', locals(), context_instance = RequestContext(request))


@login_required(redirect_field_name='next', login_url='/login/')
def KnowledgeAndAffinityMatrix1(request):
    return KnowledgeAndAffinityMatrix(request, 1)



@login_required(redirect_field_name='next', login_url='/login/')
def createAccount(request):
    titleHead = "New user registration"

    savelabel = "go (be patient)"
    otherlabel = "cancel"
    Title = "Create an account"

    if request.user.is_authenticated() == False:
        return HttpResponse("please log in first")

    try:
        LI_user = TeamMember.objects.get(pk=request.user.pk)
    except:

        return HttpResponseRedirect('/KAAM/matrix/')

    print LI_user
    menu=globalMenu

    team = LI_user.competenceTeam

    TeamLeadLoggedIn = False
    if team.TeamLead.pk == LI_user.pk:
        TeamLeadLoggedIn= True
    else:
        return HttpResponse("please log in first")


    if request.method == 'POST':
        theform = forms.Form(request.POST)
        if ('_save' in request.POST):
            if theform.is_valid():
                username = unicode(request.POST["user"])
                password = unicode(request.POST["pass"])
                cpassword = unicode(request.POST["cpass"])
                email = unicode(request.POST["email"])
                if (password != cpassword):
                    extrainfo = "Password and confirmed password are not identical <a href=/backend/createAccount/> please try again</a>"
                    return render_to_response('backend/simpleform.html', locals(),
                                              context_instance=RequestContext(request))

                try:
                    user = TeamMember.objects.create_user(username, email, password,competenceTeam = team)
                    user.competenceTeam = team
#                    user.competenceTeam = team
                    user.is_staff = True
                    user.groups.add(Group.objects.get(pk=1))
                    user.save()
                    try:
                        recipients = [email]

                        body = unicode(username) + ", welcome to the Affinity matrix\n\n"
                        body = body + "you have now an account and can log in with \n\n"
                        body = body + "Username = " + unicode(username) + "\n"
                        body = body + "password = " + unicode(password) + "\n\n"

                        body = body + "\nHave a great day \nKristof Geilenkotten \n+32 476 635876 \n(This is an automatically generated message) "

                        print body

#                        ntc_mail = NtcMail('kge@newtec.eu', recipients, 'Welcome to N.O.T.', body, bcc=cc)
                        # send the mail using the Newtec SMTP server
#                        ntc_mail.Send()
#                        print 'Mail Sent!'
                    except Exception as e:
                        return None, " ERROR sending mail " + unicode(e)

                except Exception as e:
                    extrainfo = " could not create the user " + unicode(username) + " error given :" + unicode(
                        e) + " <a href=/backend/createAccount/> please try again</a>"
                    return render_to_response('simpleform.html', locals(),
                                              context_instance=RequestContext(request))
                return HttpResponseRedirect("/KAAM/matrix")



            else:
                print "error "
                print theform.errors
                extrainfo = unicode(theform.errors)
                return render_to_response('simpleform.html', locals(), context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect("/KAAM/matrix")

    else:
        form = forms.Form()
        form.fields["user"] = forms.CharField(label="Username")
        form.fields["email"] = forms.EmailField(label="E-mail address")
        form.fields["pass"] = forms.CharField(widget=forms.PasswordInput, label="Password")
        form.fields["cpass"] = forms.CharField(widget=forms.PasswordInput, label="Password confirmation")

    return render_to_response('simpleform.html', locals(), context_instance=RequestContext(request))


@login_required(redirect_field_name='next', login_url='/login/')
def removeSkillFromTeam(request,skillId):
    titleHead = "New user registration"

    savelabel = "go (be patient)"
    otherlabel = "cancel"
    Title = "Create an account"

    if request.user.is_authenticated() == False:
        return HttpResponse("please log in first")

    try:
        LI_user = TeamMember.objects.get(pk=request.user.pk)
    except:

        return HttpResponseRedirect("/KAAM/matrix")

    print LI_user
    menu=globalMenu

    team = LI_user.competenceTeam

    TeamLeadLoggedIn = False
    if team.TeamLead.pk == LI_user.pk:
        TeamLeadLoggedIn= True
    else:
        return HttpResponse("please log in first")


    selectedSkill = Skill_CT.objects.get(pk=int(skillId))

    print selectedSkill
    selectedSkill.delete()


    return HttpResponseRedirect("/KAAM/matrix")


@login_required(redirect_field_name='next', login_url='/login/')
def addSkillToTeam(request):
    titleHead = "New Skill"

    savelabel = "go"
    otherlabel = "cancel"
    Title = "Add a skill to the team"

    if request.user.is_authenticated() == False:
        return HttpResponse("please log in first")

    try:
        LI_user = TeamMember.objects.get(pk=request.user.pk)
    except:

        return HttpResponseRedirect("/KAAM/matrix")

    print LI_user
    menu=globalMenu

    team = LI_user.competenceTeam

    TeamLeadLoggedIn = False
    if team.TeamLead.pk == LI_user.pk:
        TeamLeadLoggedIn= True
    else:
        return HttpResponse("please log in first")

    extrainfo = "<a href=\"/KAAM/addNewSkillToTeam/\" > Click here to add a Skill that is not in the list </a>"
    if request.method == 'POST':
        theform = forms.Form(request.POST)
        if ('_save' in request.POST):
            if theform.is_valid():
                skill = request.POST.getlist('skill')
                #locs= request.POST.getlist('locations')
                print "here" ,skill

                for index in skill:
                    try:
                        skillct= Skill_CT.objects.filter(competenceTeam=team).filter(skill=index)
                        print skillct

                        if not skillct:
                            selectedSkill = Skill.objects.get(pk= int(index))
                            skillct = Skill_CT( Name = unicode(selectedSkill) + " " + unicode(team),    skill = selectedSkill,   competenceTeam =team)
                            skillct.save()
                    except Exception as e:
                        print "skill not found in competence domain adding",e


                return HttpResponseRedirect("/KAAM/matrix")



            else:
                print "error "
                print theform.errors
                extrainfo = unicode(theform.errors)
                return render_to_response('simpleform.html', locals(), context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect("/KAAM/matrix")

    else:
        form = forms.Form()
        listje = []
        for u in Skill.objects.all():
            t = u.pk, unicode(u)
            listje.append(t)

        form.fields["skill"] = forms.MultipleChoiceField(choices=listje,label="Skill")

    return render_to_response('simpleform.html', locals(), context_instance=RequestContext(request))




@login_required(redirect_field_name='next', login_url='/login/')
def addNewSkillToTeam(request):
    titleHead = "New Skill"

    savelabel = "go"
    otherlabel = "cancel"
    Title = "Add a skill to the team"

    if request.user.is_authenticated() == False:
        return HttpResponse("please log in first")

    try:
        LI_user = TeamMember.objects.get(pk=request.user.pk)
    except:

        return HttpResponseRedirect("/KAAM/matrix")

    print LI_user
    menu=globalMenu

    team = LI_user.competenceTeam

    TeamLeadLoggedIn = False
    if team.TeamLead.pk == LI_user.pk:
        TeamLeadLoggedIn= True
    else:
        return HttpResponse("please log in first")

#    extrainfo = "<a href=\"/KAAM/addNewSkillToTeam/\" > Click here to add a Skill that is not in the list </a>"
    if request.method == 'POST':
        theform = forms.Form(request.POST)
        if ('_save' in request.POST):
            if theform.is_valid():
                skill = unicode(request.POST["skill"])
                print skill
                try:
                    skill2 = Skill(Name=skill,company = team.company)
                    skill2.save()
                    skillct = Skill_CT( Name = unicode(skill2) + " " + unicode(team),    skill = skill2,   competenceTeam =team)
                    skillct.save()
                except Exception as e:
                    print "skill not found in competence domain adding",e


                return HttpResponseRedirect("/KAAM/matrix")



            else:
                print "error "
                print theform.errors
                extrainfo = unicode(theform.errors)
                return render_to_response('simpleform.html', locals(), context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect("/KAAM/matrix")

    else:
        form = forms.Form()

        form.fields["skill"] = forms.CharField(label="Skill")

    return render_to_response('simpleform.html', locals(), context_instance=RequestContext(request))



