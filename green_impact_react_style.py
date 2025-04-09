# This is a React component saved as a Python file for submission/reference purposes only.
# It is not executable Python code.

react_code = """
import React, { useState } from 'react';
import { BarChart, LineChart, Wallet, Leaf, Home, User, Trees, Droplets, Wind, AlertCircle, ArrowUpRight } from 'lucide-react';

export default function GreenImpactApp() {
  const [activeTab, setActiveTab] = useState('home');
  
  const accountBalance = 12578.45;
  const savingsGoal = 15000;
  const interestRate = 3.5;
  const co2Saved = 487;
  const treesPlanted = 32;
  const waterSaved = 14752;
  const renewableEnergy = 658;

  const transactions = [
    { id: 1, date: 'Apr 7', description: 'Deposit', amount: 500, category: 'Income' },
    { id: 2, date: 'Apr 5', description: 'Solar Panel Project', amount: -200, category: 'Investment' },
    { id: 3, date: 'Apr 2', description: 'Interest Payment', amount: 36.45, category: 'Interest' },
    { id: 4, date: 'Mar 28', description: 'Reforestation Fund', amount: -150, category: 'Investment' }
  ];

  const projectAllocation = [
    { name: 'Renewable Energy', percentage: 45, color: 'bg-green-500' },
    { name: 'Reforestation', percentage: 25, color: 'bg-emerald-500' },
    { name: 'Clean Water', percentage: 20, color: 'bg-blue-500' },
    { name: 'Sustainable Agriculture', percentage: 10, color: 'bg-yellow-500' }
  ];

  return (
    <div className="flex flex-col h-screen bg-gray-50">
      {/* Full JSX content was omitted here for brevity */}
    </div>
  );
}
"""
