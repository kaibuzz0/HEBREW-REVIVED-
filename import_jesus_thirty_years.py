#!/usr/bin/env python3
"""
JESUS' THIRTY YEARS - Complete Timeline
Reconstructing the missing years of Jesus' life
From birth to ministry (0-30 CE)
Sources: Infancy Gospels, traditions, historical context
"""

import sys
sys.path.insert(0, '/root/hebrew-repo')

from complete_bible_database import CompleteBibleDatabase
import json

JESUS_THIRTY_YEARS = [
    # YEAR 0 - Birth and Infancy
    {"age": 0, "event": "Birth in Bethlehem", "source": "Canonical", "canonical": True, 
     "location": "Bethlehem", "description": "Born to Mary and Joseph, laid in manger", 
     "confidence": 1.0, "references": ["Matthew 1-2", "Luke 2"]},
    
    {"age": 0, "event": "Presentation at Temple", "source": "Canonical", "canonical": True,
     "location": "Jerusalem", "description": "Simeon and Anna prophesy",
     "confidence": 1.0, "references": ["Luke 2:22-38"]},
    
    {"age": 0, "event": "Visit of Magi", "source": "Canonical", "canonical": True,
     "location": "Bethlehem", "description": "Gold, frankincense, myrrh",
     "confidence": 0.9, "references": ["Matthew 2:1-12"]},
    
    {"age": 0, "event": "Flight to Egypt", "source": "Canonical", "canonical": True,
     "location": "Egypt", "description": "Escape from Herod's massacre",
     "confidence": 0.9, "references": ["Matthew 2:13-18"]},
    
    # YEAR 1-2 - In Egypt
    {"age": 1, "event": "Infancy in Egypt", "source": "Tradition", "canonical": False,
     "location": "Egypt (unknown)", "description": "Tradition says family stayed 1-2 years",
     "confidence": 0.6, "references": ["Coptic tradition", "Infancy Gospel of Thomas"]},
    
    # YEAR 3-7 - Return to Nazareth
    {"age": 2, "event": "Return to Nazareth", "source": "Canonical", "canonical": True,
     "location": "Nazareth", "description": "Settled in Galilee after Herod's death",
     "confidence": 0.9, "references": ["Matthew 2:19-23", "Luke 2:39"]},
    
    {"age": 5, "event": "Childhood miracles (Infancy Gospel)", "source": "Infancy Gospel of Thomas", "canonical": False,
     "location": "Nazareth", "description": "Birds from clay, raising dead child, healing wood",
     "confidence": 0.3, "references": ["Infancy Gospel of Thomas"]},
    
    {"age": 7, "event": "First teachers", "source": "Infancy Gospel", "canonical": False,
     "location": "Nazareth", "description": "Taught teachers in temple (different from age 12 incident)",
     "confidence": 0.2, "references": ["Infancy Gospel of Thomas 6-8"]},
    
    # YEAR 8-12 - Childhood
    {"age": 8, "event": "Carpentry training begins", "source": "Historical", "canonical": False,
     "location": "Nazareth", "description": "Learned father's trade (tekton)",
     "confidence": 0.7, "references": ["Mark 6:3", "Historical context"]},
    
    {"age": 10, "event": "Family life with James, Joses, Simon, Judas", "source": "Canonical", "canonical": True,
     "location": "Nazareth", "description": "Grew up with half-brothers and sisters",
     "confidence": 0.8, "references": ["Mark 6:3", "Matthew 13:55-56"]},
    
    {"age": 12, "event": "In the Temple", "source": "Canonical", "canonical": True,
     "location": "Jerusalem", "description": "Found teaching priests, 'about my Father's business'",
     "confidence": 1.0, "references": ["Luke 2:41-52"]},
    
    # YEAR 13-18 - Teenage years
    {"age": 13, "event": "Bar mitzvah", "source": "Historical", "canonical": False,
     "location": "Nazareth synagogue", "description": "Became son of the commandment",
     "confidence": 0.8, "references": ["Jewish custom"]},
    
    {"age": 14, "event": "Carpentry work", "source": "Historical", "canonical": False,
     "location": "Nazareth/Sepphoris", "description": "Worked with Joseph, possibly in nearby Sepphoris",
     "confidence": 0.6, "references": ["Archaeological: Sepphoris rebuilding"]},
    
    {"age": 15, "event": "Joseph's death (speculated)", "source": "Tradition", "canonical": False,
     "location": "Nazareth", "description": "By time of ministry, Joseph not mentioned",
     "confidence": 0.5, "references": ["Joseph absent in ministry accounts"]},
    
    {"age": 16, "event": "Took over family care", "source": "Historical", "canonical": False,
     "location": "Nazareth", "description": "As eldest, cared for Mary and siblings",
     "confidence": 0.6, "references": ["Historical context", "John 19:26-27"]},
    
    {"age": 17, "event": "Scripture study", "source": "Historical", "canonical": False,
     "location": "Nazareth synagogue", "description": "Learned Hebrew, Aramaic, possibly Greek",
     "confidence": 0.7, "references": ["Luke 4:16-20 reading", "Historical education"]},
    
    # YEAR 19-25 - Young adult
    {"age": 18, "event": "Travel to Jerusalem for festivals", "source": "Historical", "canonical": False,
     "location": "Jerusalem", "description": "Annual pilgrimages as required",
     "confidence": 0.8, "references": ["Luke 2:41", "Deuteronomy 16:16"]},
    
    {"age": 20, "event": "Witnessed John the Baptist (speculated)", "source": "Historical", "canonical": False,
     "location": "Jordan River area", "description": "May have known John before ministry",
     "confidence": 0.4, "references": ["Luke 1:36 (kinship)"]},
    
    {"age": 22, "event": "Meditation in wilderness areas", "source": "Tradition", "canonical": False,
     "location": "Judean wilderness", "description": "Preparation for ministry",
     "confidence": 0.3, "references": ["Tradition", "Desert fathers"]},
    
    {"age": 24, "event": "Interaction with Essenes (speculated)", "source": "Historical", "canonical": False,
     "location": "Qumran area", "description": "Possible connections to Essene community",
     "confidence": 0.3, "references": ["Dead Sea Scrolls parallels", "Historical speculation"]},
    
    {"age": 25, "event": "Teaching in synagogues (pre-ministry)", "source": "Canonical inference", "canonical": False,
     "location": "Galilee", "description": "Before public ministry, already known as teacher",
     "confidence": 0.5, "references": ["Luke 4:15"]},
    
    # YEAR 26-29 - Late twenties
    {"age": 26, "event": "Marriage at Cana (speculated timing)", "source": "Canonical", "canonical": True,
     "location": "Cana", "description": "First miracle, 'my hour has not yet come'",
     "confidence": 0.7, "references": ["John 2:1-11"]},
    
    {"age": 27, "event": "Baptism by John", "source": "Canonical", "canonical": True,
     "location": "Jordan River", "description": "The heavens opened, Spirit descended",
     "confidence": 1.0, "references": ["Matthew 3:13-17", "Mark 1:9-11", "Luke 3:21-22"]},
    
    {"age": 27, "event": "Temptation in wilderness", "source": "Canonical", "canonical": True,
     "location": "Wilderness", "description": "40 days, three temptations",
     "confidence": 1.0, "references": ["Matthew 4:1-11", "Luke 4:1-13"]},
    
    {"age": 28, "event": "Calling first disciples", "source": "Canonical", "canonical": True,
     "location": "Galilee", "description": "Andrew, Peter, James, John, Philip, Nathanael",
     "confidence": 1.0, "references": ["John 1:35-51", "Matthew 4:18-22"]},
    
    {"age": 28, "event": "Wedding at Cana (if different timing)", "source": "Canonical", "canonical": True,
     "location": "Cana", "description": "Water to wine",
     "confidence": 0.8, "references": ["John 2"]},
    
    {"age": 29, "event": "Early ministry in Galilee", "source": "Canonical", "canonical": True,
     "location": "Galilee", "description": "Sermon on Mount, healings, parables",
     "confidence": 1.0, "references": ["Matthew 5-7", "Mark 1-2"]},
    
    {"age": 30, "event": "Public ministry begins fully", "source": "Canonical", "canonical": True,
     "location": "Galilee/Judea", "description": "The year of favor proclaimed",
     "confidence": 1.0, "references": ["Luke 4:16-21"]},
]

# Add additional traditions and apocryphal stories
JESUS_EXTRA_TRADITIONS = [
    {"age": 12, "event": "Visit to India (Notovich tradition)", "source": "Speculative", "canonical": False,
     "location": "India/Tibet", "description": "Learned from gurus (controversial)",
     "confidence": 0.05, "references": ["Notovich 'Unknown Life' - largely discredited"]},
    
    {"age": 14, "event": "Training with Essenes", "source": "Speculative", "canonical": False,
     "location": "Qumran", "description": "Learned their teachings",
     "confidence": 0.2, "references": ["Some scholars suggest connections"]},
    
    {"age": 18, "event": "Journey to Britain (Arthurian legend)", "source": "Legend", "canonical": False,
     "location": "Glastonbury", "description": "With Joseph of Arimathea (myth)",
     "confidence": 0.0, "references": ["Medieval legend, no historical basis"]},
    
    {"age": 20, "event": "Shipbuilder in Sepphoris", "source": "Historical", "canonical": False,
     "location": "Sepphoris", "description": "Tekton could mean builder, not just carpenter",
     "confidence": 0.4, "references": ["Greek 'tekton' = craftsman/builder"]},
]

def import_jesus_timeline():
    """Import Jesus' thirty years timeline"""
    db = CompleteBibleDatabase()
    
    print("="*70)
    print("JESUS' THIRTY YEARS - COMPLETE TIMELINE")
    print("="*70)
    
    # Clear existing
    db.cursor.execute("DELETE FROM jesus_years")
    
    imported = 0
    canonical_count = 0
    
    print("\n📅 CANONICAL EVENTS:")
    for event in JESUS_THIRTY_YEARS:
        db.add_jesus_year(
            age=event["age"],
            event=event["event"],
            source=event["source"],
            canonical=event["canonical"],
            location=event["location"],
            description=event["description"],
            confidence=event["confidence"]
        )
        imported += 1
        if event["canonical"]:
            canonical_count += 1
            print(f"  Age {event['age']:2d}: {event['event']}")
    
    print(f"\n📜 EXTRA TRADITIONS:")
    for event in JESUS_EXTRA_TRADITIONS:
        db.add_jesus_year(
            age=event["age"],
            event=event["event"],
            source=event["source"],
            canonical=event["canonical"],
            location=event["location"],
            description=event["description"],
            confidence=event["confidence"]
        )
        imported += 1
        print(f"  Age {event['age']:2d}: {event['event']} [{event['source']}]")
    
    # Export
    timeline_export = {
        "title": "Jesus' Thirty Years - Complete Timeline",
        "canonical_events": [e for e in JESUS_THIRTY_YEARS if e["canonical"]],
        "extra_traditions": JESUS_EXTRA_TRADITIONS,
        "statistics": {
            "total_events": imported,
            "canonical": canonical_count,
            "historical": len([e for e in JESUS_THIRTY_YEARS if e["source"] == "Historical"]),
            "apocryphal": len([e for e in JESUS_THIRTY_YEARS + JESUS_EXTRA_TRADITIONS if not e["canonical"]])
        },
        "confidence_breakdown": {
            "high_09_10": len([e for e in JESUS_THIRTY_YEARS + JESUS_EXTRA_TRADITIONS if e["confidence"] >= 0.9]),
            "medium_05_08": len([e for e in JESUS_THIRTY_YEARS + JESUS_EXTRA_TRADITIONS if 0.5 <= e["confidence"] < 0.9]),
            "low_00_04": len([e for e in JESUS_THIRTY_YEARS + JESUS_EXTRA_TRADITIONS if e["confidence"] < 0.5])
        }
    }
    
    with open('/root/hebrew-repo/exports/jesus_thirty_years.json', 'w', encoding='utf-8') as f:
        json.dump(timeline_export, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*70)
    print("IMPORT COMPLETE")
    print("="*70)
    print(f"\n📊 Statistics:")
    print(f"   Total events: {imported}")
    print(f"   Canonical: {canonical_count}")
    print(f"   From tradition: {imported - canonical_count}")
    print(f"\n✅ Exported to exports/jesus_thirty_years.json")
    
    print("\n🎯 KEY FINDINGS:")
    print("   - 0-12 years: Well documented (canonical)")
    print("   - 12-30 years: Mostly silence in Bible")
    print("   - Gap filled by: Infancy Gospels, traditions, historical context")
    print("   - Highest confidence: Birth, Temple at 12, Baptism at 30")
    
    db.close()

if __name__ == "__main__":
    import_jesus_timeline()