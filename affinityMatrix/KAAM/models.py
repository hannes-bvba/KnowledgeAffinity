from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class ownedObject(models.Model):
    Owner = models.ForeignKey(User,verbose_name="owner of this object",on_delete=models.CASCADE)
    def __unicode__(self):
        """Make printable"""
        try:
            return self.Name
        except:
            return "erro"


class Company(ownedObject):
    Name = models.CharField("Name", max_length=30)
    def __unicode__(self):
        """Make printable"""
        return self.Name

class CompetenceTeam(ownedObject):
    Name = models.CharField("Name", max_length=30)
    company = models.ForeignKey(Company,verbose_name="The company to which this team belongs",on_delete=models.CASCADE)
    TeamLead = models.ForeignKey(User, verbose_name= "The Teamlead of this team",on_delete=models.CASCADE)

    class Meta:
        unique_together = ('Name', 'company',)

    def __unicode__(self):
        """Make printable"""
        return self.Name



class TeamMember(User):
    competenceTeam = models.ForeignKey(CompetenceTeam,verbose_name="The competence team to which this user belongs",on_delete=models.CASCADE)

    def   create_user(username, email, password,competenceTeam ):
        super(TeamMember, self).create_user(*args, **kwargs)


    def __unicode__(self):
        """Make printable"""
        return str(self.username)
#    def __unicode__(self):
#        """Make printable"""
#        return self.Name


class Skill(models.Model):
    #ToDo should be unique
    Name = models.CharField("Name", max_length=30)
    company = models.ForeignKey(Company,verbose_name="The company to which this skill belongs",on_delete=models.CASCADE)

    class Meta:
        unique_together = ('Name', 'company',)


    def __unicode__(self):
        """Make printable"""
        return self.Name

ChoiceAffinity  = ((0, ' '),(1, 'interested'), (2, 'Very interested'))

class Skill_user(models.Model):
#    Name = models.CharField("Name", max_length=30)
    skill = models.ForeignKey(Skill,verbose_name="Skill/Affinity",on_delete=models.CASCADE)
    teamMember = models.ForeignKey(TeamMember,verbose_name="Team member",on_delete=models.CASCADE)
    affinity = models.IntegerField( choices=ChoiceAffinity ,verbose_name="Affinity")
    skills = models.IntegerField(verbose_name="Skills 0=no 10=expert",validators=[MaxValueValidator(10), MinValueValidator(0)])
    def __unicode__(self):
        """Make printable"""
        return str(self.skill.Name) +" ," + str(self.teamMember) +" ," + str(self.affinity )+" ," + str(self.skills)

    def AffinityUp(self):
        self.affinity = self.affinity +1
        if self.affinity >2:
            self.affinity =2
        self.save()

    def AffinityDown(self):
        self.affinity = self.affinity -1
        if self.affinity <0:
            self.affinity =0
        self.save()


    def skillsUp(self):
        self.skills = self.skills +1
        if self.skills >10:
            self.skills =10
        self.save()

    def skillsDown(self):
        self.skills = self.skills -1
        if self.skills < 0:
            self.skills =0
        self.save()


class Skill_CT(models.Model):
    Name = models.CharField("Name", max_length=30)
    skill = models.ForeignKey(Skill,verbose_name="Skill/Affinity",on_delete=models.CASCADE)
    competenceTeam = models.ForeignKey(CompetenceTeam, verbose_name='The competence team to which this skill belongs',on_delete=models.CASCADE)

    def __unicode__(self):
        """Make printable"""
        return self.Name

