from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
d=json.loads((R/'libretv/catalog/channels.json').read_text('utf-8'))
def q(s):return str(s or '').replace('"',"'").replace('\r',' ').replace('\n',' ')
lines=['#EXTM3U','# JellyView：第01版·主流优先与分类扩充','# 综合在前；官网与视频分开；实测画质不等于原生制作画质。']
for c in d['channels']:
 a={'tvg-id':c['id'],'tvg-name':c['name'],'tvg-logo':c['logo'],'group-title':c['group'],'tvg-country':c['country'],'jellyview-area':c['area'],'jellyview-country-name':c['country_name'],'jellyview-category':c['category'],'jellyview-language':c['language'],'jellyview-edition':c['edition'],'jellyview-quality':c['quality_note'],'jellyview-web-url':c['official_url']}
 if c['country']!='CN':a['jellyview-priority']=c['curation']['tier']
 lines+=['#EXTINF:-1 '+' '.join(k+'="'+q(v)+'"'for k,v in a.items()if v)+','+c['display_name'],c['url']]
for e in d['official_pages']:lines.append('#JELLYVIEW-WEB-CHANNEL:'+json.dumps(e,ensure_ascii=False,separators=(',',':')))
(R/'libretv/feeds/LibreTV-HD-Only.m3u').write_bytes(('\r\n'.join(lines)+'\r\n').encode('utf-8'))
print(json.dumps({'video_channels':len(d['channels']),'web_entries':len(d['official_pages'])}))
