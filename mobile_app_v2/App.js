import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, TextInput, ActivityIndicator } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import AsyncStorage from '@react-native-async-storage/async-storage';

// API Configuration
const API_BASE = 'http://localhost:8080/api'; // Change to your server IP for mobile

// Torah Data Context
const TorahContext = React.createContext();

// Torah Provider Component
function TorahProvider({ children }) {
  const [torahData, setTorahData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTorahData();
  }, []);

  const fetchTorahData = async () => {
    try {
      const response = await fetch(`${API_BASE}/torah`);
      const data = await response.json();
      setTorahData(data);
      setLoading(false);
    } catch (err) {
      setError('Failed to load Torah data');
      setLoading(false);
    }
  };

  return (
    <TorahContext.Provider value={{ torahData, loading, error, refresh: fetchTorahData }}>
      {children}
    </TorahContext.Provider>
  );
}

// Home Screen - Dashboard
function HomeScreen() {
  const { torahData, loading } = React.useContext(TorahContext);

  if (loading) {
    return (
      <View style={styles.centerContainer}>
        <ActivityIndicator size="large" color="#3b82f6" />
        <Text style={styles.loadingText}>Loading Torah data...</Text>
      </View>
    );
  }

  const stats = {
    books: 5,
    verses: torahData ? Object.values(torahData).reduce((sum, b) => sum + Object.keys(b.key_verses).length, 0) : 0,
    chapters: torahData ? Object.values(torahData).reduce((sum, b) => sum + b.chapters, 0) : 0
  };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Torah Analyzer v2</Text>
        <Text style={styles.headerSubtitle}>Complete Hebrew Bible Study</Text>
      </View>

      <View style={styles.statsContainer}>
        <View style={styles.statCard}>
          <Text style={styles.statNumber}>{stats.books}</Text>
          <Text style={styles.statLabel}>Books</Text>
        </View>
        <View style={styles.statCard}>
          <Text style={styles.statNumber}>{stats.chapters}</Text>
          <Text style={styles.statLabel}>Chapters</Text>
        </View>
        <View style={styles.statCard}>
          <Text style={styles.statNumber}>{stats.verses}</Text>
          <Text style={styles.statLabel}>Verses</Text>
        </View>
      </View>

      <View style={styles.featureSection}>
        <Text style={styles.sectionTitle}>Features</Text>
        <View style={styles.featureCard}>
          <Text style={styles.featureName}>🔢 Gematria Calculator</Text>
          <Text style={styles.featureDesc}>4 methods: Standard, Katan, Gadol, Siduri</Text>
        </View>
        <View style={styles.featureCard}>
          <Text style={styles.featureName}>🌱 8 Seeds Analysis</Text>
          <Text style={styles.featureDesc}>NA HA GE OR RI VO EL AM</Text>
        </View>
        
        <View style={styles.featureCard}>
          <Text style={styles.featureName}>🤖 AI Insights</Text>
          <Text style={styles.featureDesc}>Automated pattern detection</Text>
        </View>
      </View>
    </ScrollView>
  );
}

// Books Screen
function BooksScreen({ navigation }) {
  const { torahData, loading } = React.useContext(TorahContext);

  if (loading) {
    return (
      <View style={styles.centerContainer}>
        <ActivityIndicator size="large" color="#3b82f6" />
      </View>
    );
  }

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.pageTitle}>Torah Books</Text>
      
      {torahData && Object.entries(torahData).map(([name, book]) => (
        <TouchableOpacity key={name} style={styles.bookCard}>
          <View style={styles.bookHeader}>
            <Text style={styles.bookName}>{name}</Text>
            <Text style={styles.bookHebrew}>{book.hebrew_name}</Text>
          </View>
          <Text style={styles.bookStats}>
            {book.chapters} chapters • {Object.keys(book.key_verses).length} verses
          </Text>
        </TouchableOpacity>
      ))}
    </ScrollView>
  );
}

// Gematria Calculator Screen
function CalculatorScreen() {
  const [input, setInput] = useState('');
  const [result, setResult] = useState(null);

  const calculateGematria = async () => {
    // In real implementation, would call Python backend
    // For now, simple calculation
    const hebrew = input;
    let value = 0;
    for (let char of hebrew) {
      // Simple mapping (in real app would use full gematria)
      if (char.charCodeAt(0) > 1487 && char.charCodeAt(0) < 1515) {
        value += char.charCodeAt(0) - 1487;
      }
    }
    setResult({
      standard: value,
      katan: value % 9 || 9,
      ordinal: hebrew.length
    });
  };

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.pageTitle}>Gematria Calculator</Text>
      
      <TextInput
        style={styles.input}
        placeholder="Enter Hebrew text..."
        placeholderTextColor="#94a3b8"
        value={input}
        onChangeText={setInput}
        textAlign="right"
        multiline
      />
      
      <TouchableOpacity style={styles.button} onPress={calculateGematria}>
        <Text style={styles.buttonText}>Calculate</Text>
      </TouchableOpacity>
      
      {result && (
        <View style={styles.resultContainer}>
          <View style={styles.resultCard}>
            <Text style={styles.resultValue}>{result.standard}</Text>
            <Text style={styles.resultLabel}>Standard</Text>
          </View>
          <View style={styles.resultCard}>
            <Text style={styles.resultValue}>{result.katan}</Text>
            <Text style={styles.resultLabel}>Katan</Text>
          </View>
          <View style={styles.resultCard}>
            <Text style={styles.resultValue}>{result.ordinal}</Text>
            <Text style={styles.resultLabel}>Ordinal</Text>
          </View>
        </View>
      )}
    </ScrollView>
  );
}

// Main App
const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <TorahProvider>
      <NavigationContainer>
        <Tab.Navigator
          screenOptions={{
            tabBarStyle: { backgroundColor: '#1e293b', borderTopColor: '#334155' },
            tabBarActiveTintColor: '#3b82f6',
            tabBarInactiveTintColor: '#64748b',
            headerStyle: { backgroundColor: '#0f172a' },
            headerTintColor: '#e2e8f0',
          }}
        >
          <Tab.Screen 
            name="Home" 
            component={HomeScreen} 
            options={{ title: 'Dashboard' }}
          />
          <Tab.Screen 
            name="Books" 
            component={BooksScreen}
            options={{ title: 'Torah' }}
          />
          <Tab.Screen 
            name="Calculator" 
            component={CalculatorScreen}
            options={{ title: 'Gematria' }}
          />
        </Tab.Navigator>
      </NavigationContainer>
    </TorahProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f172a',
  },
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#0f172a',
  },
  header: {
    padding: 20,
    backgroundColor: '#1e293b',
    borderBottomWidth: 1,
    borderBottomColor: '#334155',
  },
  headerTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#3b82f6',
  },
  headerSubtitle: {
    fontSize: 14,
    color: '#94a3b8',
    marginTop: 5,
  },
  loadingText: {
    color: '#94a3b8',
    marginTop: 10,
  },
  statsContainer: {
    flexDirection: 'row',
    padding: 20,
    gap: 10,
  },
  statCard: {
    flex: 1,
    backgroundColor: '#1e293b',
    borderRadius: 12,
    padding: 20,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#334155',
  },
  statNumber: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#3b82f6',
  },
  statLabel: {
    color: '#94a3b8',
    marginTop: 5,
    fontSize: 12,
  },
  featureSection: {
    padding: 20,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#e2e8f0',
    marginBottom: 15,
  },
  featureCard: {
    backgroundColor: '#1e293b',
    borderRadius: 12,
    padding: 20,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: '#334155',
  },
  featureName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#10b981',
    marginBottom: 5,
  },
  featureDesc: {
    color: '#94a3b8',
    fontSize: 14,
  },
  pageTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#e2e8f0',
    padding: 20,
  },
  bookCard: {
    backgroundColor: '#1e293b',
    borderRadius: 12,
    padding: 20,
    marginHorizontal: 20,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: '#334155',
  },
  bookHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 5,
  },
  bookName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#e2e8f0',
  },
  bookHebrew: {
    fontSize: 16,
    color: '#3b82f6',
  },
  bookStats: {
    color: '#94a3b8',
    fontSize: 14,
  },
  input: {
    backgroundColor: '#1e293b',
    borderRadius: 12,
    padding: 20,
    margin: 20,
    color: '#e2e8f0',
    fontSize: 18,
    borderWidth: 1,
    borderColor: '#334155',
    minHeight: 100,
  },
  button: {
    backgroundColor: '#3b82f6',
    borderRadius: 12,
    padding: 15,
    marginHorizontal: 20,
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  resultContainer: {
    flexDirection: 'row',
    padding: 20,
    gap: 10,
  },
  resultCard: {
    flex: 1,
    backgroundColor: '#1e293b',
    borderRadius: 12,
    padding: 20,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#3b82f6',
  },
  resultValue: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#3b82f6',
  },
  resultLabel: {
    color: '#94a3b8',
    marginTop: 5,
  },
});