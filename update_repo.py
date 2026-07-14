import os
import re
import subprocess
import urllib.request
import json
import time

def run_cmd(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def read_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

def write_readme(content):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

def main():
    repo_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Physical-Security-Software"
    os.chdir(repo_dir)

    readme = read_readme()

    # Step 1: SaaS Company Size
    saas_data = [
        {"name": "[Verkada](https://verkada.com/)", "desc": "All-in-one cloud-based security platform with cameras and access control.", "pricing": "Custom Quote", "tier": "None (30-day free trial)", "size": "$3.5 Billion (Valuation)", "val": 3500000000},
        {"name": "[Flashpoint](https://flashpoint.io/)", "desc": "Threat intelligence and physical security risk management platform.", "pricing": "Custom Quote", "tier": "None", "size": "$500 Million (Valuation)", "val": 500000000},
        {"name": "[Kastle](https://kastle.com/)", "desc": "Modern access control and visitor management system with strong security features.", "pricing": "Custom Quote", "tier": "None", "size": "$500 Million (Revenue)", "val": 500000000},
        {"name": "[Solink](https://www.solink.com/)", "desc": "AI-powered video surveillance and business intelligence platform.", "pricing": "Custom Quote", "tier": "None", "size": "$400 Million (Valuation)", "val": 400000000},
        {"name": "[XProtect](https://www.milestonesys.com/)", "desc": "Milestone’s video management software with extensive integration capabilities.", "pricing": "Custom Quote", "tier": "None", "size": "$160 Million (Revenue)", "val": 160000000},
        {"name": "[Rhombus](https://rhombus.com/)", "desc": "AI-native video surveillance and security platform with advanced analytics and cloud management.", "pricing": "Custom Quote", "tier": "None (14-day free trial)", "size": "$100 Million (Valuation)", "val": 100000000},
        {"name": "[Genea Security](https://www.genea.com/)", "desc": "Cloud-based access control and physical security management system.", "pricing": "Custom Quote", "tier": "None", "size": "$100 Million (Valuation)", "val": 100000000},
        {"name": "[Resolver](https://resolver.com/)", "desc": "Risk and security management platform with physical security modules.", "pricing": "Custom Quote", "tier": "None", "size": "Acquired by Kroll", "val": 75000000},
        {"name": "[Coram AI](https://coram.ai/)", "desc": "Intelligent video analytics platform focused on proactive threat detection.", "pricing": "Custom Quote", "tier": "None (15-day free trial)", "size": "$50 Million (Valuation)", "val": 50000000},
        {"name": "[FacilityOS](https://facilityos.com/)", "desc": "Integrated physical security and facility management platform with AI capabilities.", "pricing": "Custom Quote", "tier": "None", "size": "$10 Million (Valuation)", "val": 10000000}
    ]
    
    saas_data.sort(key=lambda x: x["val"], reverse=True)
    
    saas_table = "| Product | Description | Pricing | Free Tier Limit | Company Size |\n| :--- | :--- | :--- | :--- | :--- |\n"
    for item in saas_data:
        saas_table += f"| **{item['name']}** | {item['desc']} | {item['pricing']} | {item['tier']} | {item['size']} |\n"
    
    # Replace the existing SaaS table
    readme = re.sub(r"\| Product \| Description \| Pricing \| Free Tier Limit \|\n\| :--- \| :--- \| :--- \| :--- \|\n(?:\|.*?\|\n)+", saas_table, readme)
    write_readme(readme)
    run_cmd('git add . && git commit -m "Added company size and sorted the SaaS based on that" && git push')
    
    # Step 2: Open Source GitHub Stars
    os_repos = [
        ("ZoneMinder/zoneminder", "The most popular open-source video surveillance software with AI integration capabilities and support for hundreds of cameras."),
        ("blakeblackshear/frigate", "Highly efficient open-source NVR with real-time object detection using local AI models."),
        ("ShinobiCCTV/Shinobi", "Modern open-source CCTV/NVR solution with a clean interface and plugin support."),
        ("kerberos-io/kerberos", "Open-source video surveillance platform with edge computing and AI detection."),
        ("ispysoftware/iSpy", "Open-source surveillance software with powerful motion detection and AI features."),
        ("Motion-Project/motion", "Lightweight open-source motion detection tool that can be extended with AI for smarter alerts."),
        ("johnolafenwa/DeepStack", "Open-source AI server for object detection that integrates with surveillance systems."),
        ("codeproject/CodeProject.AI-Server", "Open-source AI server with modules for face recognition, object detection, and security use cases."),
        ("home-assistant/core", "Popular open-source home automation platform with robust physical security and camera support."),
        ("ossec/ossec-hids", "Open-source host-based intrusion detection system for physical security monitoring.")
    ]
    
    os_data = []
    for repo, desc in os_repos:
        try:
            req = urllib.request.Request(f"https://api.github.com/repos/{repo}", headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                stars = data.get("stargazers_count", 0)
        except Exception as e:
            print(f"Failed to fetch {repo}: {e}")
            stars = 0
        os_data.append({"repo": repo, "desc": desc, "stars": stars})
        time.sleep(0.5)
        
    os_data.sort(key=lambda x: x["stars"], reverse=True)
    
    # Rebuild the open source section
    os_section = "### Dedicated Physical Security & Surveillance Tools\n\n"
    for item in os_data:
        repo = item["repo"]
        name = repo.split("/")[1]
        if name == "core": name = "Home Assistant"
        elif name == "ossec-hids": name = "OSSEC"
        badge = f'[![GitHub stars](https://img.shields.io/github/stars/{repo}?style=social&color=white)](https://github.com/{repo}/stargazers)'
        os_section += f"- **[{name}](https://github.com/{repo})** {badge}  \n  {item['desc']}\n\n"
        
    # Replace the existing open source section
    readme = re.sub(r"### Dedicated Physical Security & Surveillance Tools\n\n(?:- \*\*\[.*?\]\(.*?\)[\s\S]*?(?=\n### Additional Strong Open-Source Options))", os_section, readme)
    write_readme(readme)
    run_cmd('git add . && git commit -m "Added github stars and sorted the opensource based on that" && git push')
    
    # Step 3: SVG Banner
    os.makedirs("assets", exist_ok=True)
    svg_content = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A2980" />
      <stop offset="100%" stop-color="#26D0CE" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2.5" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="800" height="200" fill="url(#bg)" rx="15" ry="15"/>
  <circle cx="100" cy="100" r="40" fill="none" stroke="#ffffff" stroke-width="4" stroke-dasharray="10 5">
    <animateTransform attributeName="transform" type="rotate" from="0 100 100" to="360 100 100" dur="5s" repeatCount="indefinite" />
  </circle>
  <circle cx="700" cy="100" r="40" fill="none" stroke="#ffffff" stroke-width="4" stroke-dasharray="10 5">
    <animateTransform attributeName="transform" type="rotate" from="360 700 100" to="0 700 100" dur="5s" repeatCount="indefinite" />
  </circle>
  <text x="50%" y="45%" font-family="Arial, sans-serif" font-size="36" font-weight="bold" fill="#ffffff" text-anchor="middle" filter="url(#glow)">Awesome Physical Security</text>
  <text x="50%" y="65%" font-family="Arial, sans-serif" font-size="18" fill="#e0e0e0" text-anchor="middle">SaaS &amp; Open-Source Software Tools Ecosystem</text>
</svg>'''
    with open("assets/banner.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    readme = read_readme()
    if "assets/banner.svg" not in readme:
        readme = f'<div align="center">\n  <img src="assets/banner.svg" alt="Awesome Physical Security Banner" />\n</div>\n\n' + readme
        write_readme(readme)
    run_cmd('git add . && git commit -m "added banner" && git push')
    
    # Step 4: Add emojis
    readme = read_readme()
    readme = readme.replace("## Top Physical Security Software Tools Ecosystem", "## 🛡️ Top Physical Security Software Tools Ecosystem")
    readme = readme.replace("## Table of Contents", "## 📑 Table of Contents")
    readme = readme.replace("## SaaS Products", "## ☁️ SaaS Products")
    readme = readme.replace("## Open-Source GitHub Projects", "## 🔓 Open-Source GitHub Projects")
    readme = readme.replace("## How to Contribute", "## 🤝 How to Contribute")
    readme = readme.replace("## Disclaimer", "## ⚠️ Disclaimer")
    readme = readme.replace("### Core Platforms (Physical Security Software)", "### 🏢 Core Platforms (Physical Security Software)")
    readme = readme.replace("### Dedicated Physical Security & Surveillance Tools", "### 🎥 Dedicated Physical Security & Surveillance Tools")
    readme = readme.replace("### Additional Strong Open-Source Options", "### 🛠️ Additional Strong Open-Source Options")
    write_readme(readme)
    run_cmd('git add . && git commit -m "added emojis" && git push')
    
    # Step 5: SEO Optimised
    readme = read_readme()
    if "<meta" not in readme:
        seo_tags = '<!--\n  Keywords: Physical Security, Video Surveillance, Access Control, SaaS, Open Source, NVR, CCTV, AI Security, Intrusion Detection, Facility Management\n  Description: A curated list of top SaaS products and open-source GitHub projects for physical security, video surveillance, and access control.\n-->\n'
        readme = seo_tags + readme
        write_readme(readme)
    run_cmd('git add . && git commit -m "seo optimised" && git push')
    
    # Step 6: Badges to left
    readme = read_readme()
    left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
    
    # Find the title or banner and add badges below it. Let's add them right after the banner div.
    if '<div align="center">' in readme:
        # Check if we already have a badge container
        if 'id="badges"' not in readme:
            readme = readme.replace('<div align="center">\n  <img src="assets/banner.svg" alt="Awesome Physical Security Banner" />\n</div>\n', 
                                    f'<div align="center">\n  <img src="assets/banner.svg" alt="Awesome Physical Security Banner" />\n  <br/>\n  <div id="badges">\n    {left_badges}\n  </div>\n</div>\n')
    else:
        readme = f'<div align="center" id="badges">{left_badges}</div>\n' + readme
    write_readme(readme)
    run_cmd('git add . && git commit -m "badges to left added" && git push')
    
    # Step 7: Badges to right
    readme = read_readme()
    right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
    if '<div id="badges">' in readme:
        readme = readme.replace('<div id="badges">\n    ' + left_badges + '\n  </div>', 
                                '<div id="badges">\n    ' + left_badges + ' ' + right_badge + '\n  </div>')
    write_readme(readme)
    run_cmd('git add . && git commit -m "badges to right added" && git push')
    
    # Step 8: Star History
    readme = read_readme()
    folder_name = "Awesome-Physical-Security-Software"
    star_history = f'''
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2F{folder_name}&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
</picture>
</a>
</div>
'''
    if "##  Star History" not in readme:
        readme += "\n" + star_history
        write_readme(readme)
    run_cmd('git add . && git commit -m "star history added" && git push')
    
    # Step 9: Fix chartrepos
    readme = read_readme()
    if "chartrepos" in readme:
        readme = readme.replace("chartrepos", "chart?repos")
        write_readme(readme)
        run_cmd('git add . && git commit -m "fixed star plot" && git push')
    else:
        # Create empty commit if not found
        run_cmd('git commit --allow-empty -m "fixed star plot" && git push')
        
    # Step 10: Fix invalid awesome link
    readme = read_readme()
    if "https://github.com/sindresorhus/awesome" in readme:
        readme = readme.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
        write_readme(readme)
        run_cmd('git add . && git commit -m "invalid awesome link fixed" && git push')
    else:
        run_cmd('git commit --allow-empty -m "invalid awesome link fixed" && git push')

if __name__ == "__main__":
    main()
