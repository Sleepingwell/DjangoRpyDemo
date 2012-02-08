from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms

try:
    from rpy2.robjects import globalEnv
except:
    from rpy2.robjects import globalenv as globalEnv

from rpy2.robjects import r as R

import random

resultDir = "static/results/"

# might be better call source on a file or load a package here.
R("""renderer <- function(filename, title, units) {
    dat <- rnorm(1000)
    png(file=filename, width=720, height=480)
    hist(dat, main=title, xlab=units)
    dev.off()
}""")


def index(request):
    return render_to_response('index.html', {'form': MainForm()}, context_instance=RequestContext(request))


class MainForm(forms.Form):
    seriesTypes = [('rainfall', 'mm'), ('elevation', 'm')]
    seriesTypes = map(lambda x: ("%s_%s" % (x[0], x[1]), "%s (%s)" % (x[0], x[1])), seriesTypes)
    series = forms.ChoiceField(choices=seriesTypes, widget=forms.Select(attrs={'onchange': 'selectSite()'}))
    site = forms.ChoiceField(widget=forms.Select(attrs={'onchange': 'doJobby()', 'disabled': 'disabled'}))


def getSites(request):
    (seriesType, units) = request.GET["value"].split("_")
    availableSites = [('site1a', 'site1'), ('site2a', 'site2')]
    availableSites = map(lambda x: ("%s|%s" % (x[0], x[1]), x[1]), availableSites)
    response = render_to_response("sites_list.html", {'sites': availableSites})
    response.set_cookie("seriesType", seriesType)
    response.set_cookie("units", units)
    return response


def doFDC(request):
    (siteId, siteName) = request.GET["value"].split("|")
    (seriesType, units) = (request.COOKIES["seriesType"], request.COOKIES["units"])
    filename = "%d_%s" % (random.randint(1000, 9999), "boxplot.png")
    R.renderer(resultDir + filename, "Random data for site %s (%s)" % (siteName, units), units)
    return HttpResponse('<img src="/static/results/' + filename + '" />')
