"""由公开频道目录生成精选、扩充订阅及兼容配置，不联网测流。"""
from pathlib import Path
from urllib.parse import urlsplit
import argparse
import json

ROOT=Path(__file__).resolve().parents[2]
DEFAULT_BASE='https://raw.githubusercontent.com/sq666-ca/JellyView/main'

def main():
    parser=argparse.ArgumentParser(description='生成JellyView直播订阅和LibreTV兼容配置')
    parser.add_argument('--base-url',default=DEFAULT_BASE,help='同时提供订阅与台标的HTTP(S)资料根地址')
    args=parser.parse_args()
    base=args.base_url.rstrip('/')
    parts=urlsplit(base)
    if parts.scheme not in ['http','https'] or not parts.netloc or parts.query or parts.fragment:
        parser.error('资料根地址必须是无查询参数的HTTP(S)地址')
    selection=json.loads((ROOT/'libretv/catalog/selection.json').read_text('utf-8'))
    logos=json.loads((ROOT/'libretv/catalog/logos.json').read_text('utf-8'))
    by_id={x['id']:x for x in logos['entries']}
    def logo(row):
        asset=by_id[row['id']].get('asset')
        return base+'/'+asset if asset else ''
    def quote(value):return str(value or '').replace('"',"'").replace('\r',' ').replace('\n',' ')
    for kind,filename,title,canonical in [('Selected','channels.json','主流覆盖与特色精选','LibreTV-HD-Only.m3u'),('Expansion','expansion.json','扩充备选','JellyView-Expansion.m3u')]:
        data=json.loads((ROOT/'libretv/catalog'/filename).read_text('utf-8'))
        lines=['#EXTM3U',f"# JellyView：第{selection['release']}版·{title}；发布{selection['published_at']}；测流{selection['checked_on']}"]
        for c in data['channels']:
            attrs={'tvg-id':c['id'],'tvg-name':c['name'],'tvg-logo':logo(c),'group-title':c['group'],'tvg-country':c['country'],'jellyview-area':c['area'],'jellyview-country-name':c['country_name'],'jellyview-category':c['category'],'jellyview-language':c['language'],'jellyview-edition':c['edition'],'jellyview-quality':c['quality_note'],'jellyview-web-url':c.get('official_url',''),'jellyview-short-name':by_id[c['id']]['short_name'],'jellyview-status':c['status'],'jellyview-checked-on':selection['checked_on']}
            if c['country']!='CN':attrs['jellyview-priority']=c['curation']['tier']
            lines+=['#EXTINF:-1 '+' '.join(k+'="'+quote(v)+'"' for k,v in attrs.items() if v)+','+c['display_name'],c['url']]
        for page in data['official_pages']:
            page=dict(page,logo=logo(page),shortName=by_id[page['id']]['short_name'])
            lines.append('#JELLYVIEW-WEB-CHANNEL:'+json.dumps(page,ensure_ascii=False,separators=(',',':')))
        playlist=('\r\n'.join(lines)+'\r\n').encode('utf-8')
        (ROOT/f'libretv/feeds/JellyView-{kind}.m3u').write_bytes(playlist)
        entry={'name':'JellyView·'+title,'url':base+'/libretv/feeds/'+canonical,'epg':''}
        config={'name':'JellyView直播·第'+selection['release']+'版·'+title,'version':2,'description':f"发布{selection['published_at']}；测流{selection['checked_on']}；{len(data['channels'])}路视频、{len(data['official_pages'])}个独立官网入口；画质和可用性反映检测时段。",'liveSources':[entry],'live':[entry],'sources':[]}
        config_text=json.dumps(config,ensure_ascii=False,indent=2)+'\n'
        (ROOT/f'libretv/feeds/JellyView-{kind}.json').write_text(config_text,'utf-8')
        if kind=='Selected':
            (ROOT/'libretv/feeds/LibreTV-HD-Only.m3u').write_bytes(playlist)
            (ROOT/'libretv/feeds/LibreTV-HD-Only.json').write_text(config_text,'utf-8')
        print(kind,len(data['channels']),len(data['official_pages']))

if __name__=='__main__':main()
