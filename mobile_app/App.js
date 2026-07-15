import React, { useState, useEffect } from 'react';
import { 
  View, 
  Text, 
  TextInput, 
  ScrollView, 
  StyleSheet,
  TouchableOpacity,
  SafeAreaView,
  StatusBar
} from 'react-native';

// Hebrew Bible Analyzer - React Native App
// This is a web-compatible version that can run in browser

export default function App() {
  const [hebrewText, setHebrewText] = useState('בראשית ברא אלהים');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);

  // Simple gematria calculation (for demo)
  const calculateGematria = (text) => {
    const values = {
      'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
      'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90,
      'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400,
      'ך': 20, 'ם': 40, 'ן': 50, 'ף': 80, 'ץ': 90
    };
    
    let total = 0;
    for (let char of text) {
      total += values[char] || 0;
    }
    return total;
  };

  const analyzeText = () => {
    setLoading(true);
    
    // Simulate analysis
    const words = hebrewText.split(' ');
    const wordAnalysis = words.map(word => ({
      word: word,
      gematria: calculateGematria(word),
      // Simple seed detection
      seeds: detectSeeds(word)
    }));
    
    const total = wordAnalysis.reduce((sum, w) => sum + w.gematria, 0);
    
    setAnalysis({
      words: wordAnalysis,
      totalGematria: total,
      wordCount: words.length
    });
    
    setLoading(false);
  };

  const detectSeeds = (word) => {
    // Simplified seed detection
    const seeds = [];
    if (word.includes('אל')) seeds.push('EL');
    if (word.includes('ה')) seeds.push('HA');
    if (word.includes('ו')) seeds.push('VO');
    if (word.includes('מ')) seeds.push('AM');
    if (word.includes('ר')) seeds.push('RI');
    return seeds.length > 0 ? seeds.join(' → ') : 'NA';
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="light-content" backgroundColor="#0d1117" />
      
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.title}>🔯 Hebrew Bible Analyzer</Text>
        <Text style={styles.subtitle}>Gematria • Seeds • Torah</Text>
      </View>

      <ScrollView style={styles.scrollView}>
        {/* Stats Cards */}
        <View style={styles.statsContainer}>
          <View style={styles.statCard}>
            <Text style={styles.statNumber}>5</Text>
            <Text style={styles.statLabel}>Books</Text>
          </View>
          <View style={styles.statCard}>
            <Text style={styles.statNumber}>44</Text>
            <Text style={styles.statLabel}>Verses</Text>
          </View>
          <View style={styles.statCard}>
            <Text style={styles.statNumber}>8</Text>
            <Text style={styles.statLabel}>Seeds</Text>
          </View>
        </View>

        {/* Input Section */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Analyze Hebrew Text</Text>
          <TextInput
            style={styles.input}
            value={hebrewText}
            onChangeText={setHebrewText}
            placeholder="Enter Hebrew text..."
            placeholderTextColor="#666"
            multiline
          />
          <TouchableOpacity 
            style={styles.button}
            onPress={analyzeText}
            disabled={loading}
          >
            <Text style={styles.buttonText}>
              {loading ? 'Analyzing...' : 'Analyze'}
            </Text>
          </TouchableOpacity>
        </View>

        {/* Results */}
        {analysis && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Results</Text>
            <View style={styles.totalCard}>
              <Text style={styles.totalLabel}>Total Gematria</Text>
              <Text style={styles.totalValue}>{analysis.totalGematria}</Text>
              <Text style={styles.totalSublabel}>{analysis.wordCount} words analyzed</Text>
            </View>
            
            {analysis.words.map((word, index) => (
              <View key={index} style={styles.wordCard}>
                <Text style={styles.hebrewWord}>{word.word}</Text>
                <View style={styles.wordDetails}>
                  <Text style={styles.gematriaValue}>Gematria: {word.gematria}</Text>
                  <Text style={styles.seedValue}>Seeds: {word.seeds}</Text>
                </View>
              </View>
            ))}
          </View>
        )}

        {/* Seeds Reference */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>8 Seeds Reference</Text>
          <View style={styles.seedsGrid}>
            {[
              {symbol: 'NA', name: 'Sacred Stillness'},
              {symbol: 'HA', name: 'Living Breath'},
              {symbol: 'GE', name: 'Sacred Form'},
              {symbol: 'OR', name: 'Unveiling Light'},
              {symbol: 'RI', name: 'Turning Alignment'},
              {symbol: 'VO', name: 'Sounded Truth'},
              {symbol: 'EL', name: 'Seal / Witness'},
              {symbol: 'AM', name: 'Embodiment'},
            ].map((seed, index) => (
              <View key={index} style={styles.seedCard}>
                <Text style={styles.seedSymbol}>{seed.symbol}</Text>
                <Text style={styles.seedName}>{seed.name}</Text>
              </View>
            ))}
          </View>
        </View>

        {/* Torah Books */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Torah Books</Text>
          {[
            {name: 'Genesis', hebrew: 'בראשית', verses: 8},
            {name: 'Exodus', hebrew: 'שמות', verses: 12},
            {name: 'Leviticus', hebrew: 'ויקרא', verses: 7},
            {name: 'Numbers', hebrew: 'במדבר', verses: 6},
            {name: 'Deuteronomy', hebrew: 'דברים', verses: 11},
          ].map((book, index) => (
            <View key={index} style={styles.bookCard}>
              <View style={styles.bookHeader}>
                <Text style={styles.bookName}>{book.name}</Text>
                <Text style={styles.bookHebrew}>{book.hebrew}</Text>
              </View>
              <Text style={styles.bookVerses}>{book.verses} key verses</Text>
            </View>
          ))}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0d1117',
  },
  header: {
    backgroundColor: '#161b22',
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#30363d',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#58a6ff',
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 14,
    color: '#8b949e',
    textAlign: 'center',
    marginTop: 5,
  },
  scrollView: {
    flex: 1,
  },
  statsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    padding: 15,
  },
  statCard: {
    backgroundColor: '#161b22',
    borderRadius: 8,
    padding: 15,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#30363d',
    minWidth: 80,
  },
  statNumber: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#58a6ff',
  },
  statLabel: {
    fontSize: 12,
    color: '#8b949e',
    marginTop: 5,
  },
  section: {
    padding: 15,
    marginBottom: 10,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#c9d1d9',
    marginBottom: 15,
  },
  input: {
    backgroundColor: '#0d1117',
    borderWidth: 1,
    borderColor: '#30363d',
    borderRadius: 8,
    padding: 15,
    color: '#c9d1d9',
    fontSize: 16,
    minHeight: 60,
    textAlign: 'right',
  },
  button: {
    backgroundColor: '#238636',
    borderRadius: 8,
    padding: 15,
    marginTop: 10,
    alignItems: 'center',
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
  },
  totalCard: {
    backgroundColor: '#238636',
    borderRadius: 8,
    padding: 20,
    alignItems: 'center',
    marginBottom: 15,
  },
  totalLabel: {
    color: 'white',
    fontSize: 14,
    opacity: 0.9,
  },
  totalValue: {
    color: 'white',
    fontSize: 36,
    fontWeight: 'bold',
    marginVertical: 5,
  },
  totalSublabel: {
    color: 'white',
    fontSize: 12,
    opacity: 0.8,
  },
  wordCard: {
    backgroundColor: '#161b22',
    borderRadius: 8,
    padding: 15,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: '#30363d',
  },
  hebrewWord: {
    fontSize: 24,
    color: '#c9d1d9',
    textAlign: 'center',
    marginBottom: 10,
  },
  wordDetails: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  gematriaValue: {
    color: '#58a6ff',
    fontSize: 14,
  },
  seedValue: {
    color: '#238636',
    fontSize: 14,
  },
  seedsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  seedCard: {
    backgroundColor: '#161b22',
    borderRadius: 8,
    padding: 15,
    marginBottom: 10,
    width: '48%',
    borderWidth: 1,
    borderColor: '#30363d',
    alignItems: 'center',
  },
  seedSymbol: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#58a6ff',
  },
  seedName: {
    fontSize: 12,
    color: '#8b949e',
    marginTop: 5,
    textAlign: 'center',
  },
  bookCard: {
    backgroundColor: '#161b22',
    borderRadius: 8,
    padding: 15,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: '#30363d',
  },
  bookHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  bookName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#c9d1d9',
  },
  bookHebrew: {
    fontSize: 18,
    color: '#58a6ff',
  },
  bookVerses: {
    fontSize: 12,
    color: '#8b949e',
    marginTop: 5,
  },
});